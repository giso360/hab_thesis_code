import csv
import random
from statistics import mode
import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as pltu
import csv


def shuffle_and_trim_list(alist, elements):
    random.shuffle(alist)
    return alist[:elements]

# 1. Collect All Labeled Pixels

img = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/TC.jpeg')

print(img.shape)
print(img.size)

# TLWH
hab_from_high_hab_xml = [559, 549, 564, 250]
no_hab_from_high_hab_xml = [319, 1733, 510, 184]

Sep_2021_HAB = []
Sep_2021_NO_HAB = []


for i in range(hab_from_high_hab_xml[0], hab_from_high_hab_xml[0] + hab_from_high_hab_xml[3]):
    for j in range(hab_from_high_hab_xml[1], hab_from_high_hab_xml[1] + hab_from_high_hab_xml[2]):
        # img[i, j] = [0, 0, 255]  # Draw HAB areas in
        Sep_2021_HAB.append([i, j])


for i in range(no_hab_from_high_hab_xml[0], no_hab_from_high_hab_xml[0] + no_hab_from_high_hab_xml[3]):
    for j in range(no_hab_from_high_hab_xml[1], no_hab_from_high_hab_xml[1] + no_hab_from_high_hab_xml[2]):
        # img[i, j] = [255, 0, 0]  # Draw no_HAB areas in green
        Sep_2021_NO_HAB.append([i, j])


# 2. Keep 5K only, save to csv and verify

Sep_2021_HAB_5K = shuffle_and_trim_list(Sep_2021_HAB, 5000)
Sep_2021_NO_HAB_5K = shuffle_and_trim_list(Sep_2021_NO_HAB, 5000)

with open('Sep_2021_HAB_5K.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerows(Sep_2021_HAB_5K)

with open('Sep_2021_NO_HAB_5K.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerows(Sep_2021_NO_HAB_5K)

Sep_2021_HAB_5K_FROM_FILE = []

file1 = open('Sep_2021_HAB_5K.csv')
csvreader1 = csv.reader(file1)
for row in csvreader1:
    Sep_2021_HAB_5K_FROM_FILE.append(row)
for hab_pixel in Sep_2021_HAB_5K_FROM_FILE:
    img[int(hab_pixel[0]), int(hab_pixel[1])] = [0, 0, 255]
Sep_2021_NO_HAB_5K_FROM_FILE = []
file2 = open('Sep_2021_NO_HAB_5K.csv')
csvreader2 = csv.reader(file2)
for row in csvreader2:
    Sep_2021_NO_HAB_5K_FROM_FILE.append(row)
for hab_pixel in Sep_2021_NO_HAB_5K_FROM_FILE:
    img[int(hab_pixel[0]), int(hab_pixel[1])] = [255, 0, 0]








cv.namedWindow("image", cv.WINDOW_NORMAL)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

# A2. find modes B01, B03, B05 with pixel set => no_hab_pixels_from_HIGH_HAB_TC

# take 5K

# img_B01 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B5.jpeg', 0)
#
# print("print pixels")
# print(img_B01.shape[0])
# print(img_B01.shape[1])
#
# count = 0
# HIGH_HAB_NO_HAB_5K = shuffle_and_trim_list(no_hab_pixels_from_HIGH_HAB_TC, 5000)
# HIGH_HAB_HAB_5K = shuffle_and_trim_list(hab_pixels_from_HIGH_HAB_TC, 5000)
#
#
# print(HIGH_HAB_NO_HAB_5K)
#
# with open('high_hab_random_No_Hab.csv', 'w', newline='') as f:
#     write = csv.writer(f)
#     write.writerows(HIGH_HAB_NO_HAB_5K)
#
# with open('high_hab_random_Hab.csv', 'w', newline='') as f:
#     write = csv.writer(f)
#     write.writerows(HIGH_HAB_HAB_5K)

# B01s = []
#
# for pixel in bb:
#     B01s.append(img_B01[pixel[0]][pixel[1]])
#
#
# print("MODE IS:")
# print(mode(B01s))

# no_hab_HIGH_HAB_5K = shuffle_and_trim_list(no_hab_pixels_from_HIGH_HAB_TC, 5000)
# print(no_hab_HIGH_HAB_5K)
# print(str(len(no_hab_HIGH_HAB_5K)))
#
# for pixel in no_hab_HIGH_HAB_5K:
#     B01s.append(img_B01[pixel[0], pixel[1]])
#     img_B01[pixel[0], pixel[1]] = [0]

# cv.namedWindow("image", cv.WINDOW_NORMAL)
# cv.imshow('image', img_B01)
# cv.waitKey(0)
# cv.destroyAllWindows()

