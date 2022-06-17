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

# 1. Process Image

# A. HIGH HAB IMAGE
img = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/TC.jpeg')

print(img.shape)
print(img.size)

# TLWH
hab_from_high_hab_xml = [559, 549, 564, 250]
no_hab_from_high_hab_xml = [319, 1733, 510, 184]

hab_pixels_from_HIGH_HAB_TC = []
no_hab_pixels_from_HIGH_HAB_TC = []


for i in range(hab_from_high_hab_xml[0], hab_from_high_hab_xml[0] + hab_from_high_hab_xml[3]):
    for j in range(hab_from_high_hab_xml[1], hab_from_high_hab_xml[1] + hab_from_high_hab_xml[2]):
        img[i, j] = [0, 0, 255]  # Draw HAB areas in
        hab_pixels_from_HIGH_HAB_TC.append([i,j])


for i in range(no_hab_from_high_hab_xml[0], no_hab_from_high_hab_xml[0] + no_hab_from_high_hab_xml[3]):
    for j in range(no_hab_from_high_hab_xml[1], no_hab_from_high_hab_xml[1] + no_hab_from_high_hab_xml[2]):
        img[i, j] = [255, 0, 0]  # Draw no_HAB areas in green
        no_hab_pixels_from_HIGH_HAB_TC.append([i,j])

# print("HAB pixels FROM HIGH HAB IMAGE !!!")
# print(hab_pixels_from_HIGH_HAB_TC)
# print("HAB pixels are: " + str(len(hab_pixels_from_HIGH_HAB_TC)))

# print("NO HAB pixels FROM HIGH HAB IMAGE !!!")
# print(no_hab_pixels_from_HIGH_HAB_TC)
# print("HAB pixels are: " + str(len(no_hab_pixels_from_HIGH_HAB_TC)))

# cv.namedWindow("image", cv.WINDOW_NORMAL)
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# A2. find modes B01, B03, B05 with pixel set => no_hab_pixels_from_HIGH_HAB_TC

# take 5K

img_B01 = cv.imread('../dataset/HIGH_HAB/06_09_2021/images/narrowband/B5.jpeg', 0)

print("print pixels")
print(img_B01.shape[0])
print(img_B01.shape[1])

count = 0
HIGH_HAB_NO_HAB_5K = shuffle_and_trim_list(no_hab_pixels_from_HIGH_HAB_TC, 5000)
HIGH_HAB_HAB_5K = shuffle_and_trim_list(hab_pixels_from_HIGH_HAB_TC, 5000)


print(HIGH_HAB_NO_HAB_5K)

with open('high_hab_random_No_Hab.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerows(HIGH_HAB_NO_HAB_5K)

with open('high_hab_random_Hab.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerows(HIGH_HAB_HAB_5K)

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

cv.namedWindow("image", cv.WINDOW_NORMAL)
cv.imshow('image', img_B01)
cv.waitKey(0)
cv.destroyAllWindows()


# B. LOW HAB IMAGE

# 1. Process Image

# img = cv.imread('../dataset/LOW_HAB/22_08_2020/images/TC.jpeg')
# print(img.shape)
# print(img.size)
#
# # TLWH
#
# hab_from_low_hab_xml = [619, 589, 525, 205]
# no_hab_from_low_hab_xml = [849, 1519, 235, 365]
#
# hab_pixels_from_LOW_HAB_TC = []
# no_hab_pixels_from_LOW_HAB_TC = []
#
#
# for i in range(hab_from_low_hab_xml[0], hab_from_low_hab_xml[0] + hab_from_low_hab_xml[3]):
#     for j in range(hab_from_low_hab_xml[1], hab_from_low_hab_xml[1] + hab_from_low_hab_xml[2]):
#         img[i, j] = [0, 0, 255]  # Draw HAB areas in
#         hab_pixels_from_LOW_HAB_TC.append([i,j])
#
# for i in range(no_hab_from_low_hab_xml[0], no_hab_from_low_hab_xml[0] + no_hab_from_low_hab_xml[3]):
#     for j in range(no_hab_from_low_hab_xml[1], no_hab_from_low_hab_xml[1] + no_hab_from_low_hab_xml[2]):
#         img[i, j] = [255, 0, 0]  # Draw no_HAB areas in green
#         no_hab_pixels_from_LOW_HAB_TC.append([i,j])
#
# print("HAB pixels FROM LOW HAB IMAGE !!!")
# print(hab_pixels_from_LOW_HAB_TC)
# print("HAB pixels are: " + str(len(hab_pixels_from_LOW_HAB_TC)))
#
# print("NO HAB pixels FROM LOW HAB IMAGE !!!")
# print(no_hab_pixels_from_LOW_HAB_TC)
# print("HAB pixels are: " + str(len(no_hab_pixels_from_LOW_HAB_TC)))
#
# cv.namedWindow("image", cv.WINDOW_NORMAL)
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
#
#
#
