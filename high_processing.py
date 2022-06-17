import csv
import random
from statistics import mode
import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as pltu
import csv

features = ["B01",
            "B02",
            "B03",
            "B04",
            "B05",
            "B06",
            "B07",
            "B08",
            "B08A",
            "B09",
            "B11",
            "B12",
            "NDCI",
            "NDVI",
            "NDVI_B8A",
            "MPHBI",
            "RD1",
            "RD2",
            "RD3",
            "CLASS"
            ]

mode_B01 = 11
mode_B03 = 12
mode_B05 = 4

def NDCI_feature(B04, B05):
    if B04 + B05 == 0:
        return 0
    return round(abs((int(B05)-int(B04))/(int(B05)+int(B04))), 2)


def NDVI_feature(B04, B08):
    if B04 + B08 == 0:
        return 0
    return round(abs((int(B08)-int(B04))/(int(B08)+int(B04))), 2)


def NDVI_B8A_feature(B04, B08A):
    if B04 + B08A == 0:
        return 0
    return round(abs((int(B08A)-int(B04))/(int(B08)+int(B04))), 2)


def MPHBI_feature(B04, B05, B06, B08):
    T1 = round(abs((int(B05)-int(B04)) - (int(B06)-int(B05)) * 0.5333), 2)
    T2 = round(abs((int(B06)-int(B04)) - (int(B08)-int(B04)) * 0.4237), 2)
    if T1 == T2:
        return T1
    return max(T1, T2)


def RD1_feature(B01):
    return abs(mode_B01 - B01)


def RD2_feature(B03):
    return abs(mode_B03 - B03)


def RD3_feature(B05):
    return abs(mode_B05 - B05)


img1 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B1.jpeg', 0)
img2 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B2.jpeg', 0)
img3 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B3.jpeg', 0)
img4 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B4.jpeg', 0)
img5 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B5.jpeg', 0)
img6 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B6.jpeg', 0)
img7 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B7.jpeg', 0)
img8 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B8.jpeg', 0)
img8A = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B8A.jpeg', 0)
img9 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B9.jpeg', 0)
img11 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B11.jpeg', 0)
img12 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B12.jpeg', 0)



# HAB PIXELS

Sep_2021_HAB_5K = []    # HAB pixels for Aug_2020
Sep_2021_HAB_5K_features = []
file1 = open('./pixels5k/Sep_2021_HAB_5K.csv')
csvreader1 = csv.reader(file1)
for row in csvreader1:
    class_number = 1    # HAB == 1
    row = [int(row[0]), int(row[1])]
    Sep_2021_HAB_5K.append(row)
    feature_vector = []
    B01 = img1[row[0]][row[1]]
    feature_vector.append(B01)
    B02 = img2[row[0]][row[1]]
    feature_vector.append(B02)
    B03 = img3[row[0]][row[1]]
    feature_vector.append(B03)
    B04 = img4[row[0]][row[1]]
    feature_vector.append(B04)
    B05 = img5[row[0]][row[1]]
    feature_vector.append(B05)
    B06 = img6[row[0]][row[1]]
    feature_vector.append(B06)
    B07 = img7[row[0]][row[1]]
    feature_vector.append(B07)
    B08 = img8[row[0]][row[1]]
    feature_vector.append(B08)
    B08A = img8A[row[0]][row[1]]
    feature_vector.append(B08A)
    B09 = img9[row[0]][row[1]]
    feature_vector.append(B09)
    B11 = img11[row[0]][row[1]]
    feature_vector.append(B11)
    B12 = img12[row[0]][row[1]]
    feature_vector.append(B12)
    NDCI = NDCI_feature(B04, B05)
    feature_vector.append(NDCI)
    NDVI = NDVI_feature(B04, B08)
    feature_vector.append(NDVI)
    NDVI_B08A = NDVI_B8A_feature(B04, B08A)
    feature_vector.append(NDVI_B08A)
    MPHBI = MPHBI_feature(B04, B05, B06, B08)
    feature_vector.append(MPHBI)
    RD1 = RD1_feature(B01)
    feature_vector.append(RD1)
    RD2 = RD2_feature(B03)
    feature_vector.append(RD2)
    RD3 = RD3_feature(B05)
    feature_vector.append(RD3)
    feature_vector.append(class_number)
    Sep_2021_HAB_5K_features.append(feature_vector)


# Load to CSV
with open('./numerical_dataset/Sep_2021_HAB.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(features)
    write.writerows(Sep_2021_HAB_5K_features)


# #############
# NO_HAB PIXELS
# #############

Sep_2021_NO_HAB_5K = []    # NO_HAB pixels for Aug_2020
Sep_2021_NO_HAB_5K_features = []
file2 = open('./pixels5k/Sep_2021_NO_HAB_5K.csv')
csvreader2 = csv.reader(file2)
for row in csvreader2:
    class_number = 0    # NO_HAB == 0
    row = [int(row[0]), int(row[1])]
    Sep_2021_NO_HAB_5K.append(row)
    feature_vector = []
    B01 = img1[row[0]][row[1]]
    feature_vector.append(B01)
    B02 = img2[row[0]][row[1]]
    feature_vector.append(B02)
    B03 = img3[row[0]][row[1]]
    feature_vector.append(B03)
    B04 = img4[row[0]][row[1]]
    feature_vector.append(B04)
    B05 = img5[row[0]][row[1]]
    feature_vector.append(B05)
    B06 = img6[row[0]][row[1]]
    feature_vector.append(B06)
    B07 = img7[row[0]][row[1]]
    feature_vector.append(B07)
    B08 = img8[row[0]][row[1]]
    feature_vector.append(B08)
    B08A = img8A[row[0]][row[1]]
    feature_vector.append(B08A)
    B09 = img9[row[0]][row[1]]
    feature_vector.append(B09)
    B11 = img11[row[0]][row[1]]
    feature_vector.append(B11)
    B12 = img12[row[0]][row[1]]
    feature_vector.append(B12)
    NDCI = NDCI_feature(B04, B05)
    feature_vector.append(NDCI)
    NDVI = NDVI_feature(B04, B08)
    feature_vector.append(NDVI)
    NDVI_B08A = NDVI_B8A_feature(B04, B08A)
    feature_vector.append(NDVI_B08A)
    MPHBI = MPHBI_feature(B04, B05, B06, B08)
    feature_vector.append(MPHBI)
    RD1 = RD1_feature(B01)
    feature_vector.append(RD1)
    RD2 = RD2_feature(B03)
    feature_vector.append(RD2)
    RD3 = RD3_feature(B05)
    feature_vector.append(RD3)
    feature_vector.append(class_number)
    Sep_2021_NO_HAB_5K_features.append(feature_vector)


# Load to CSV
with open('./numerical_dataset/Sep_2021_NO_HAB.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(features)
    write.writerows(Sep_2021_NO_HAB_5K_features)









