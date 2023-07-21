#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import os
import numpy as np

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('video', frame)
  key = cv2.waitKey(1)
  if key != -1:
    break
cap.release()
cv2.destroyAllWindows()
