#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2022 Chikara Hanakawa                                                                                                                                                                              
# SPDX-FileCopyrightText: 2022 Chikara Hanakawa
# SPDX-License-Identifier: BSD-3-Clause

import cv2
import os
import numpy as np

dirname = 'face_images'

cap = cv2.VideoCapture(0)

cascade_filepath = "/data/haarcascades/haarcascade_frontalface_alt.xml"
FaceCascade = cv2.CascadeClassifier(cascade_filepath)

count = 0

while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  Face = FaceCascade.detectMultiScale(gray,1.1,3,minSize=(100,100))
  if not os.path.exists(dirname):
    os.mkdir(dirname)

  for (x,y,w,h) in Face:
    count += 1
    count_padded = '%05d' % count
    cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),thickness=2)
    write_file = count_padded + ".png"
    cv2.imwrite(os.path.join(dirname, write_file), frame)

  cv2.imshow('result', frame)

  key = cv2.waitKey(1)
  if key != -1:
    break

cv2.destroyAllWindows()
cap.release()
