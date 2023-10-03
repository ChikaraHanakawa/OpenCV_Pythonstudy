#!/usr/bin/python3
import cv2
import numpy as np

#演習1
img_src = cv2.imread("/home/chikara/Pictures/lena.jpeg", 1)
resize_img = cv2.resize(img_src, dsize=(2219, 2880))
cv2.namedWindow('resize', cv2.WINDOW_NORMAL)
cv2.imshow('resize', resize_img)

#演習2
gray_img = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('grayscale', cv2.WINDOW_NORMAL)
cv2.imshow('grayscale', gray_img)

#演習3

cv2.waitKey(0)
cv2.destroyAllWindows()