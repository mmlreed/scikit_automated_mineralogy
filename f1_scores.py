import cv2
import numpy as np
import os

os.chdir('accuracy')

# Paths to test maps and clipped portios of predicted mineral maps
paths = [
    ('1_13a_rf.tif', '1_13a_test.tif'),
    ('6_3a_rf.tif', '6_3a_test.tif'),
    ('16_2a_rf.tif', '16_2a_test.tif')
]

# Mineral class mapping for each sample -- 9 is a dummy for NaNs
mineral_classes = [1, 2, 3, 4, 5, 6, 7, 8]

min_range = np.arange(np.max(mineral_classes))

mean_F1_scores = []
F1_scores1 = []

for rf_path, test_path in paths:
    RF = cv2.imread(rf_path,cv2.IMREAD_ANYDEPTH)
    TEST = cv2.imread(test_path,cv2.IMREAD_ANYDEPTH)

    # This is to ensure that all NaNs from various types of TIF formats (int8, uint8, etc.) are set to the dummy class
    RF[TEST == 0] = 9
    RF[TEST == 127] = 9
    RF[RF == 127] = 9
    RF[RF == 255] = 9
    RF[RF == 0] = 9
    RF[RF == 15] = 9;
    RF[TEST == 15] = 9;

    TEST[TEST == 127] = 9
    TEST[TEST == 0] = 9
    TEST[TEST == 255] = 9
    TEST[TEST == 15] = 9


    accuracy = np.zeros(8)
    actual = np.zeros(8)
    total_test = np.zeros(8)
    total_rf = np.zeros(8)
    F1_scores = np.zeros(8)
    F1_w = np.zeros(8)

    # loop to calculate F1 score for each mineral and the frequency-weighted F1 score for the sample
    for n in min_range:
        RF_1 = np.copy(RF)
        TEST_1 = np.copy(TEST)
        RF_1[RF_1 != mineral_classes[n]] = 0
        RF_1[RF_1 == mineral_classes[n]] = 1
        TEST_1[TEST_1 != mineral_classes[n]] = 0
        TEST_1[TEST_1 == mineral_classes[n]] = 1
        diff2 = cv2.absdiff(RF_1, TEST_1)
        wrong = np.sum(diff2)  # FP + FN
        COMB_1 = RF_1 + TEST_1
        TP = np.sum(COMB_1) / 2
        actual = np.sum(TEST_1)
        total_rf[n] = np.sum(RF_1) / (np.count_nonzero(RF) - np.count_nonzero(RF[RF == 9])) * 100
        total_test[n] = actual.astype(np.float64) / (np.count_nonzero(TEST) - np.count_nonzero(TEST[TEST == 9]))
        accuracy[n] = (1 - (wrong / actual)) * 100
        F1_scores[n] = (2 * TP) / (2 * TP + wrong)
        F1_w[n] = F1_scores[n]*total_test[n];
    F1_scores1.append(F1_scores)
    mean_F1_scores.append(np.mean(np.sum(F1_w[:8])))

print("Mean F1 Scores:", mean_F1_scores)

F1_1_13 = F1_scores1[0]
F1_6_3 = F1_scores1[1]
F1_16_2 = F1_scores1[2]

# These are hardcoded values for the minerals (unfortunately)

mean_F1_bio = np.mean([F1_6_3[0], F1_16_2[4], F1_1_13[0]])
stderr_F1_bio = np.std([F1_6_3[0], F1_16_2[4], F1_1_13[0]]) / 3

mean_F1_plag = np.mean([F1_6_3[4], F1_16_2[1], F1_1_13[1]])
stderr_F1_plag = np.std([F1_6_3[4], F1_16_2[1], F1_1_13[1]]) / 3

mean_F1_qtz = np.mean([F1_6_3[5], F1_16_2[6], F1_1_13[3]])
stderr_F1_qtz = np.std([F1_6_3[5], F1_16_2[6], F1_1_13[3]]) / 3

mean_F1_kspar = np.mean([F1_6_3[3], F1_16_2[5], F1_1_13[2]])
stderr_F1_kspar = np.std([F1_6_3[3], F1_16_2[5], F1_1_13[2]]) / 3

mean_F1_horn = np.mean([F1_6_3[2], F1_16_2[0], F1_1_13[6]])
stderr_F1_horn = np.std([F1_6_3[2], F1_16_2[0], F1_1_13[6]]) / 3

mean_F1_Fe = np.mean([F1_6_3[1], F1_16_2[2], F1_1_13[4]])
stderr_F1_Fe = np.std([F1_6_3[1], F1_16_2[2], F1_1_13[4]]) / 3

mean_F1_ap = np.mean([F1_6_3[6], F1_16_2[3], F1_1_13[5]])
stderr_F1_ap = np.std([F1_6_3[6], F1_16_2[3], F1_1_13[5]]) / 3

mean_F1_chlor = np.mean([F1_6_3[7], F1_16_2[7], F1_1_13[7]])
stderr_F1_chlor = np.std([F1_6_3[7], F1_16_2[7], F1_1_13[7]]) / 3

os.chdir('..')
