# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:26:33 2024

@author: miles
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cmcrameri.cm as cmc

# Calculate abundance error from mean F1 score of the mineral -- f1_scores.py needs run 1st

err = [bio - (bio * (1 - mean_F1_bio)), plag - (plag * (1 - mean_F1_plag)),
          qtz - (qtz * (1 - mean_F1_qtz)), kfs - (kfs * (1 - mean_F1_kspar)),
          horn - (horn * (1 - mean_F1_horn)), Fe - (Fe * (1 - mean_F1_Fe)),
          ap - (ap * (1 - mean_F1_ap)), chlor - (chlor * (1 - mean_F1_chlor))]

# Can be calculated from either side
err_bio = -err[0] + bio
err_plag = -err[1] + plag
err_qtz = -err[2] + qtz
err_kfs = -err[3] + kfs
err_horn = -err[4] + horn
err_Fe = -err[5] + Fe
err_ap = -err[6] + ap
err_chlor = -err[7] + chlor

# Mineral names
bio_string = "Biotite"
plag_string = "Plagioclase"
qtz_string = "Quartz"
kfs_string = "K-spar"
horn_string = "Hornblende"
fe_string = "Fe-Ti"
ap_string = "Apatite"
chlor_string = "Chlorite"

# Data strucutres for each mineral w/ name, abundance values, and errors
bio_plot = [bio_string] + list(bio) + list(err_bio)
plag_plot = [plag_string] + list(plag) + list(err_plag)
qtz_plot = [qtz_string] + list(qtz) + list(err_qtz)
kfs_plot = [kfs_string] + list(kfs) + list(err_kfs)
horn_plot = [horn_string] + list(horn) + list(err_horn)
fe_plot = [fe_string] + list(Fe) + list(err_Fe)
ap_plot = [ap_string] + list(ap) + list(err_ap)
chlor_plot = [chlor_string] + list(chlor) + list(err_chlor)

# Create pandas dataframe
df = pd.DataFrame([bio_plot, plag_plot, qtz_plot, kfs_plot, horn_plot, fe_plot, ap_plot, chlor_plot],
                  columns=['Mineral', '1-1a', '1-1b', '1-13a', '1-13b', '1-21a', '1-21b','2-2a', '2-2b',
                           '6-3a', '6-3b', '8-3a', '8-3b', '16-2a','16-2b',
                           'err_1-1a', 'err_1-1b', 'err_1-13a', 'err_1-13b', 'err_1-21a', 'err_1-21b','err_2-2a', 'err_2-2b',
                           'err_6-3a', 'err_6-3b', 'err_8-3a', 'err_8-3b', 'err_16-2a','err_16-2b'])

# Get errors into right format for yerr in pandas bar plot with numpy
errors = df[['err_1-1a', 'err_1-1b', 'err_1-13a', 'err_1-13b', 'err_1-21a', 'err_1-21b','err_2-2a', 'err_2-2b',
'err_6-3a', 'err_6-3b', 'err_8-3a', 'err_8-3b', 'err_16-2a','err_16-2b']].to_numpy().T


font_properties1 = {'family': 'Arial', 'size': 16}
plt.rc('font', **font_properties1)

fig, ax = plt.subplots(figsize=(8, 6), linewidth=2)

colormap = cmc.batlow

ax = df[['Mineral','1-1a', '1-1b', '1-13a', '1-13b', '1-21a', '1-21b','2-2a', '2-2b', '6-3a', '6-3b', '8-3a', '8-3b', '16-2a','16-2b']].plot(x='Mineral',
        kind='bar',
        stacked=False,
        colormap=colormap,
        edgecolor='black',
        ax=ax,
        yerr=errors,
        rot=0)

# We used 'Helvetica Light' here, but most people will not have that supremely elegant font
# probably will default to DejaVu Sans in Linux
font_properties2 = {'family': 'Arial', 'size': 18}

ax.set_ylabel('Abundance (areal %)', fontdict=font_properties2)
ax.set_xlabel('Mineral', fontdict=font_properties2)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, title='Sample')

plt.tight_layout()
plt.show()



