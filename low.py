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

img = cv.imread('../dataset/LOW_HAB/22_08_2020/images/TC.jpeg')

print(img.shape)
print(img.size)

# TLWH
hab_from_low_hab_xml = [619, 589, 525, 205]
no_hab_from_low_hab_xml = [849, 1519, 235, 365]

Aug_2020_HAB = []
Aug_2020_NO_HAB = []


for i in range(hab_from_low_hab_xml[0], hab_from_low_hab_xml[0] + hab_from_low_hab_xml[3]):
    for j in range(hab_from_low_hab_xml[1], hab_from_low_hab_xml[1] + hab_from_low_hab_xml[2]):
        # img[i, j] = [0, 0, 255]  # Draw HAB areas in
        Aug_2020_HAB.append([i, j])


for i in range(no_hab_from_low_hab_xml[0], no_hab_from_low_hab_xml[0] + no_hab_from_low_hab_xml[3]):
    for j in range(no_hab_from_low_hab_xml[1], no_hab_from_low_hab_xml[1] + no_hab_from_low_hab_xml[2]):
        # img[i, j] = [255, 0, 0]  # Draw no_HAB areas in green
        Aug_2020_NO_HAB.append([i, j])


# 2. Keep 5K only, save to csv and verify

Aug_2020_HAB_5K = shuffle_and_trim_list(Aug_2020_HAB, 5000)
Aug_2020_NO_HAB_5K = shuffle_and_trim_list(Aug_2020_NO_HAB, 5000)

with open('Aug_2020_HAB_5K.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerows(Aug_2020_HAB_5K)

with open('Aug_2020_NO_HAB_5K.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerows(Aug_2020_NO_HAB_5K)

Aug_2020_HAB_5K_FROM_FILE = []
file1 = open('Aug_2020_HAB_5K.csv')
csvreader1 = csv.reader(file1)
for row in csvreader1:
    Aug_2020_HAB_5K_FROM_FILE.append(row)
for hab_pixel in Aug_2020_HAB_5K_FROM_FILE:
    img[int(hab_pixel[0]), int(hab_pixel[1])] = [0, 0, 255]

Aug_2020_NO_HAB_5K_FROM_FILE = []
file2 = open('Aug_2020_NO_HAB_5K.csv')
csvreader2 = csv.reader(file2)
for row in csvreader2:
    Aug_2020_NO_HAB_5K_FROM_FILE.append(row)
for hab_pixel in Aug_2020_NO_HAB_5K_FROM_FILE:
    img[int(hab_pixel[0]), int(hab_pixel[1])] = [255, 0, 0]








cv.namedWindow("image", cv.WINDOW_NORMAL)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
