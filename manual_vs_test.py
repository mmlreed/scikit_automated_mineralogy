import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import os

os.chdir('accuracy')

# Load images
RF = cv2.imread('6_3a_rf.tif', cv2.IMREAD_GRAYSCALE)
TEST = cv2.imread('6_3a_test.tif', cv2.IMREAD_GRAYSCALE)

# Convert pixel values to int8
RF = np.int8(RF)
TEST = np.int8(TEST)

# Set specific pixel values to 9
RF[np.isin(RF, [127, 255, 0, 15])] = 9
TEST[np.isin(TEST, [127, 0, 255, 15])] = 9

# Convert mineral order from 6-3a to a universal order
# Mineral order 6-3: Ap=7-->17; Bio=1-->11; Chlor=8-->18; Fe=2-->16; Horn=3-->15; Kspar=4-->14; Plag=5-->12; Qtz=6-->13
RF_conversion_map = {1: 11, 2: 16, 3: 15, 4: 14, 5: 12, 6: 13, 7: 17, 8: 18, 9:19}
RF = np.vectorize(RF_conversion_map.get)(RF)

TEST_conversion_map = {1: 11, 2: 16, 3: 15, 4: 14, 5: 12, 6: 13, 7: 17, 8: 18, 9:19}
TEST = np.vectorize(TEST_conversion_map.get)(TEST)

# Calculate the count of non-constant pixels in TEST and RF
ALL_test = np.sum(TEST[TEST != 19])
ALL_rf = np.sum(RF[RF != 19])

# Calculate individual mineral ratios in TEST and RF
BIO_rf = np.sum(RF[RF == 11]) / ALL_rf
PLAG_rf = np.sum(RF[RF == 12]) / ALL_rf
QTZ_rf = np.sum(RF[RF == 13]) / ALL_rf
KSPAR_rf = np.sum(RF[RF == 14]) / ALL_rf
HORN_rf = np.sum(RF[RF == 15]) / ALL_rf
FE_rf = np.sum(RF[RF == 16]) / ALL_rf
AP_rf = np.sum(RF[RF == 17]) / ALL_rf
CHL_rf = np.sum(RF[RF == 18]) / ALL_rf

BIO_test = np.sum(TEST[TEST == 11]) / ALL_test
PLAG_test = np.sum(TEST[TEST == 12]) / ALL_test
QTZ_test = np.sum(TEST[TEST == 13]) / ALL_test
KSPAR_test = np.sum(TEST[TEST == 14]) / ALL_test
HORN_test = np.sum(TEST[TEST == 15]) / ALL_test
FE_test = np.sum(TEST[TEST == 16]) / ALL_test
AP_test = np.sum(TEST[TEST == 17]) / ALL_test
CHL_test = np.sum(TEST[TEST == 18]) / ALL_test

RF6_3_pts = [BIO_rf*100, PLAG_rf*100, QTZ_rf*100, HORN_rf*100, KSPAR_rf*100, FE_rf*100, AP_rf*100, CHL_rf*100]
TEST6_3_pts = [BIO_test*100, PLAG_test*100, QTZ_test*100, HORN_test*100, KSPAR_test*100, FE_test*100, AP_test*100, CHL_test*100]




RF1 = RF.flatten()
TEST1 = TEST.flatten()
C_6_3 = confusion_matrix(TEST1, RF1)
C_6_3 = C_6_3[:8, :8]


# Load the images
RF = cv2.imread('16_2a_rf.tif', cv2.IMREAD_ANYDEPTH)
TEST = cv2.imread('16_2a_test.tif', cv2.IMREAD_ANYDEPTH)

# Convert the images to int8
RF = np.int8(RF)
TEST = np.int8(TEST)

# Replace specific pixel values with 9
RF[np.isin(RF, [127, 255, 0, 15])] = 9
TEST[np.isin(TEST, [127, 0, 255, 15])] = 9

# Convert mineral order from 16-2 to a universal order
# Mineral order 16-2: Ap=4; Bio=5; Chlor=8; Fe=3; Horn=1; Kspar=6; Plag=2; Qtz=7
# bio=11, plag=12, qtz=13, kfs=14, horn=15, Fe=16, ap=17, chlor=18
RF_conversion_map = {1: 15, 2: 12, 3: 16, 4: 17, 5: 11, 6: 14, 7: 13, 8: 18, 9:19}
RF = np.vectorize(RF_conversion_map.get)(RF)

TEST_conversion_map = {1: 15, 2: 12, 3: 16, 4: 17, 5: 11, 6: 14, 7: 13, 8: 18, 9:19}
TEST = np.vectorize(TEST_conversion_map.get)(TEST)

# Calculate the count of non-constant pixels in TEST and RF
ALL_test = np.sum(TEST[TEST != 19])
ALL_rf = np.sum(RF[RF != 19])

# Calculate individual mineral ratios in TEST and RF
BIO_rf = np.sum(RF[RF == 11]) / ALL_rf
PLAG_rf = np.sum(RF[RF == 12]) / ALL_rf
QTZ_rf = np.sum(RF[RF == 13]) / ALL_rf
KSPAR_rf = np.sum(RF[RF == 14]) / ALL_rf
HORN_rf = np.sum(RF[RF == 15]) / ALL_rf
FE_rf = np.sum(RF[RF == 16]) / ALL_rf
AP_rf = np.sum(RF[RF == 17]) / ALL_rf
CHL_rf = np.sum(RF[RF == 18]) / ALL_rf

BIO_test = np.sum(TEST[TEST == 11]) / ALL_test
PLAG_test = np.sum(TEST[TEST == 12]) / ALL_test
QTZ_test = np.sum(TEST[TEST == 13]) / ALL_test
KSPAR_test = np.sum(TEST[TEST == 14]) / ALL_test
HORN_test = np.sum(TEST[TEST == 15]) / ALL_test
FE_test = np.sum(TEST[TEST == 16]) / ALL_test
AP_test = np.sum(TEST[TEST == 17]) / ALL_test
CHL_test = np.sum(TEST[TEST == 18]) / ALL_test

RF16_2_pts = [BIO_rf*100, PLAG_rf*100, QTZ_rf*100, HORN_rf*100, KSPAR_rf*100, FE_rf*100, AP_rf*100, CHL_rf*100]
TEST16_2_pts = [BIO_test*100, PLAG_test*100, QTZ_test*100, HORN_test*100, KSPAR_test*100, FE_test*100, AP_test*100, CHL_test*100]




RF2 = RF.flatten()
TEST2 = TEST.flatten()
C_16_2 = confusion_matrix(TEST2, RF2)
C_16_2 = C_16_2[:8, :8]


# Load the images
RF = cv2.imread('1_13a_rf.tif', cv2.IMREAD_ANYDEPTH)
TEST = cv2.imread('1_13a_test.tif', cv2.IMREAD_ANYDEPTH)

# Convert the images to int8
RF = np.int8(RF)
TEST = np.int8(TEST)

# Replace specific pixel values with 9
RF[np.isin(RF, [127, 255, 0, 15])] = 9
TEST[np.isin(TEST, [127, 0, 255, 15])] = 9

# Convert mineral order from 1-13 to a universal order
# Mineral order 1-13: Bio=1-->11; Plag=2-->12; Kfs=3-->14; Qtz=4-->13; Fe=5-->16; Ap=6-->17; Horn=7-->15; Chlor=8-->18
RF_conversion_map = {1: 11, 2: 12, 3: 14, 4: 13, 5: 16, 6: 17, 7: 15, 8: 18, 9: 19}
RF = np.vectorize(RF_conversion_map.get)(RF)

TEST_conversion_map = {1: 11, 2: 12, 3: 14, 4: 13, 5: 16, 6: 17, 7: 15, 8: 18, 9: 19}
TEST = np.vectorize(TEST_conversion_map.get)(TEST)

# Calculate the count of non-constant pixels in TEST and RF
ALL_test = np.sum(TEST[TEST != 19])
ALL_rf = np.sum(RF[RF != 19])

# Calculate individual mineral ratios in TEST and RF
BIO_rf = np.sum(RF[RF == 11]) / ALL_rf
PLAG_rf = np.sum(RF[RF == 12]) / ALL_rf
QTZ_rf = np.sum(RF[RF == 13]) / ALL_rf
KSPAR_rf = np.sum(RF[RF == 14]) / ALL_rf
HORN_rf = np.sum(RF[RF == 15]) / ALL_rf
FE_rf = np.sum(RF[RF == 16]) / ALL_rf
AP_rf = np.sum(RF[RF == 17]) / ALL_rf
CHL_rf = np.sum(RF[RF == 18]) / ALL_rf

BIO_test = np.sum(TEST[TEST == 11]) / ALL_test
PLAG_test = np.sum(TEST[TEST == 12]) / ALL_test
QTZ_test = np.sum(TEST[TEST == 13]) / ALL_test
KSPAR_test = np.sum(TEST[TEST == 14]) / ALL_test
HORN_test = np.sum(TEST[TEST == 15]) / ALL_test
FE_test = np.sum(TEST[TEST == 16]) / ALL_test
AP_test = np.sum(TEST[TEST == 17]) / ALL_test
CHL_test = np.sum(TEST[TEST == 18]) / ALL_test

RF1_13_pts = [BIO_rf*100, PLAG_rf*100, QTZ_rf*100, HORN_rf*100, KSPAR_rf*100, FE_rf*100, AP_rf*100, CHL_rf*100]
TEST1_13_pts = [BIO_test*100, PLAG_test*100, QTZ_test*100, HORN_test*100, KSPAR_test*100, FE_test*100, AP_test*100, CHL_test*100]

RF3 = RF.flatten()
TEST3 = TEST.flatten()
C_1_13 = confusion_matrix(TEST3, RF3)
C_1_13 = C_1_13[:8, :8]


# Combining confusion matrices
COMB = C_6_3 + C_16_2 + C_1_13

colors=[0,1,2,3,4,5,6,7]

# Scatter plots for comparison -- Figure 5 in manuscript w/ viridis colors -- custom colors w/ minerals in legend in manuscript
plt.scatter(TEST6_3_pts, RF6_3_pts, c=colors, s=80, marker='o', edgecolors='black', label='6-3a', cmap='viridis')
plt.scatter(TEST16_2_pts, RF16_2_pts, c=colors,s=80, marker='s', edgecolors='black', label='16-2a',cmap='viridis')
plt.scatter(TEST1_13_pts, RF1_13_pts, c=colors, s=80, marker='d', edgecolors='black', label='1-13a',cmap='viridis')

plt.plot(np.linspace(*plt.xlim()), np.linspace(*plt.ylim()), color='black')  # Diagonal line

plt.legend()
plt.xlabel('Manually mapped mineral abundance (%)')
plt.ylabel('RF-predicted mineral abundance (%)')
plt.show()

os.chdir('..')

