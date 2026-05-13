
# Calculate mineral abundance from majority-filtered, rf-predicted maps

import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

bio = np.zeros(14)
plag = np.zeros(14)
qtz = np.zeros(14)
kfs = np.zeros(14)
horn = np.zeros(14)
Fe = np.zeros(14)
ap = np.zeros(14)
chlor = np.zeros(14)

max_val = np.zeros(14)

samp_names = ['1-1a', '1-1b', '1-13a', '1-13b', '1-21a', '1-21b', '2-2a', '2-2b', '6-3a', '6-3b', '8-3a', '8-3b', '16-2a', '16-3b']

os.chdir('maps')

# folder with mineral maps

for i in range(14):
    min_img = cv2.imread(f'{i + 1}_rf_pred_maj10_clip_uint8.tif', cv2.IMREAD_ANYDEPTH)

    # uint8 NaN -- should all be uint8 tifs
    nan_val = 15

    min_names = np.empty((1, 8, 14), dtype='U10')

    # Assign values to min_names manually
    min_names[0, :, 0] = ["plag", "horn", "qtz", "kfs", "bio", "Fe", "ap", "chlor"]
    min_names[0,:,1] = ["ap","bio","chlor","Fe","horn","kfs","plag","qtz"]

    min_names[0,:,2] = ["bio","plag","kfs","qtz","Fe","ap","horn","chlor"];
    min_names[0,:,3] = ["plag","kfs","bio","qtz","horn","Fe","ap","chlor"];

    min_names[0,:,4] = ["bio","plag","horn","Fe","ap","kfs","qtz","chlor"];
    min_names[0,:,5] = ["bio","plag","qtz","kfs","horn","Fe","ap","chlor"];

    min_names[0,:,6] = ["plag","bio","horn","qtz","kfs","ap","Fe","chlor"];
    min_names[0,:,7] = ["plag","bio","qtz","kfs","horn","Fe","ap","chlor"];

    min_names[0,:,8] = ["bio","Fe","horn","kfs","plag","qtz","ap","chlor"];
    min_names[0,:,9] = ["plag","bio","qtz","kfs","horn","Fe","ap","chlor"];

    min_names[0,:,10] = ["plag","qtz","bio","kfs","ap","horn","Fe","chlor"];
    min_names[0,:,11] = ["plag","qtz","kfs","horn","bio","Fe","ap","chlor"];

    min_names[0,:,12] = ["horn","plag","Fe","ap","bio","kfs","qtz","chlor"];
    min_names[0,:,13] = ["plag","qtz","kfs","bio","horn","ap","Fe","chlor"];


    min_img[min_img > 8] = 15

    total_pix_full = np.prod(min_img.shape)
    nan_pix_full = np.sum(min_img[min_img == nan_val]) / nan_val
    total_pix_sans_nans = total_pix_full - nan_pix_full

    total_rf_full = np.zeros(8)
    for n in range(8):
        min_img1 = np.copy(min_img)
        min_img1[min_img1 != (n + 1)] = 0
        min_img1[min_img1 == (n + 1)] = 1
        total_rf_full[n] = np.sum(np.sum(min_img1)) / total_pix_sans_nans * 100

    bio_num = np.where(min_names[:, :, i] == "bio")[1].item()
    plag_num = np.where(min_names[:, :, i] == "plag")[1].item()
    qtz_num = np.where(min_names[:, :, i] == "qtz")[1].item()
    kfs_num = np.where(min_names[:, :, i] == "kfs")[1].item()
    horn_num = np.where(min_names[:, :, i] == "horn")[1].item()
    Fe_num = np.where(min_names[:, :, i] == "Fe")[1].item()
    ap_num = np.where(min_names[:, :, i] == "ap")[1].item()
    chlor_num = np.where(min_names[:, :, i] == "chlor")[1].item()

    bio[i] = total_rf_full[bio_num]
    plag[i] = total_rf_full[plag_num]
    qtz[i] = total_rf_full[qtz_num]
    kfs[i] = total_rf_full[kfs_num]
    horn[i] = total_rf_full[horn_num]
    Fe[i] = total_rf_full[Fe_num]
    ap[i] = total_rf_full[ap_num]
    chlor[i] = total_rf_full[chlor_num]

os.chdir('..')


