#!/usr/bin/python3
import cv2
import math
import numpy as np

img_src = cv2.imread("/home/chikara/c++/opencv-4.5.5/OpenCV_Cppstudy/images/ball.JPG", 1)
img_dst = cv2.resize(img_src, dsize=(500, 500))
cv2.namedWindow('dst')
cv2.imshow('dst', img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
