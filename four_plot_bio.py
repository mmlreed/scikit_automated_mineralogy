import matplotlib.pyplot as plt
import numpy as np
import pickle


def load(filename):
    # Get global dictionary
    glob = globals()
    with open(filename, 'rb') as f:
        for k, v in pickle.load(f).items():
            # Set each global variable to the value from the file
            glob[k] = v

filename = 'fourplot.pkl'

load(filename)

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Subplot 1 - grain area
a = [a_1_1a.flatten().tolist(), a_6_3b.flatten().tolist()]
x = np.arange(1, 3)
colors = [[37/255, 120/255, 225/255], [255/255, 92/255, 0/255]]
line_width = 1.5

bplot1 = axs[0, 0].boxplot(a, positions=x, patch_artist=True, widths=0.5, boxprops=dict(facecolor='none', linewidth=line_width))
for patch, color in zip(bplot1['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)

for whisker, cap, median in zip(bplot1['whiskers'], bplot1['caps'], bplot1['medians']):
    whisker.set_linewidth(line_width)
    cap.set_linewidth(line_width)
    median.set_linewidth(line_width)

axs[0, 0].tick_params(axis='both', which='major', labelsize=12)
axs[0, 0].tick_params(axis='both', which='minor', labelsize=12)
axs[0, 0].set_xticklabels(['1-1a', '6-3b'])
axs[0, 0].set_ylabel('Grain area (mm$^2$)')

# Subplot 2 - neighbor grain number
a1 = [neighbs_1_1.flatten().tolist(), neighbs_6_3.flatten().tolist()]
x1 = np.arange(1, 3)

bplot2 = axs[0, 1].boxplot(a1, positions=x1, patch_artist=True, widths=0.5, boxprops=dict(facecolor='none', linewidth=line_width))
for patch, color in zip(bplot2['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)

for whisker, cap, median in zip(bplot2['whiskers'], bplot2['caps'], bplot2['medians']):
    whisker.set_linewidth(line_width)
    cap.set_linewidth(line_width)
    median.set_linewidth(line_width)

axs[0, 1].tick_params(axis='both', which='major', labelsize=12)
axs[0, 1].tick_params(axis='both', which='minor', labelsize=12)
axs[0, 1].set_xticklabels(['1-1a', '6-3b'])
axs[0, 1].set_ylabel('Neighbor grains')

# Subplot 3 - Euclidean distance transforms between biotite pixels in microns

dist11 = dist1[~np.isnan(dist1)]
dist21 = dist2[~np.isnan(dist2)]

dist11_range = np.max(dist11) - np.min(dist11)
dist21_range = np.max(dist21) - np.min(dist21)
bin_width = 75
num_bins1 = int(np.ceil(dist11_range / bin_width))
num_bins2 = int(np.ceil(dist21_range / bin_width))


# Hack to get MATLAB-like 'probability' norm -- again, could just use seaborn
# the bin edges are slightly different in manuscript plot but the underlying data is the same
counts1, bins1 = np.histogram(dist11, bins=num_bins1)
counts_weighter1=counts1.sum()
counts2, bins2 = np.histogram(dist21, bins=num_bins2)
counts_weighter2=counts2.sum()

axs[1, 0].hist(bins1[:-1],bins=num_bins1,weights=counts1/counts_weighter1, histtype='step', linewidth=2, label='1-1a')
axs[1, 0].hist(bins2[:-1],bins=num_bins2,weights=counts2/counts_weighter2, histtype='step', linewidth=2, label='6-3b')
axs[1, 0].set_xlabel('Distance to biotite (µm)')
axs[1, 0].set_ylabel('Normalized frequency (%)')
axs[1,0].legend()


# Subplot 4 - fraction of neighbor grains around biotite by mineral
values = np.array([[frac_plag, frac_plag2], [frac_qtz, frac_qtz2], [frac_kfs, frac_kfs2], [frac_horn, frac_horn2], [frac_Fe, frac_Fe2], [frac_ap, frac_ap2], [frac_chlor, frac_chlor2]])
values_reshaped = values.reshape(7, 2)

x1 = np.arange(values_reshaped.shape[0])
bar_width = 0.25

x_labels = ['Plagioclase', 'Quartz', 'K-spar', 'Hornblende', 'Fe-Ti', 'Apatite', 'Chlorite']
for i in range(values_reshaped.shape[1]):
    axs[1,1].bar(x1 + i * bar_width, values_reshaped[:, i], width=bar_width, edgecolor='black')

axs[1, 1].tick_params(axis='both', which='major', labelsize=12)
axs[1, 1].tick_params(axis='both', which='minor', labelsize=12)
axs[1,1].set_xticks(x1 + bar_width / 2)
axs[1,1].set_xticklabels(x_labels, rotation=30)
axs[1, 1].set_ylabel('Neighbor fraction')

plt.tight_layout()
plt.show()
