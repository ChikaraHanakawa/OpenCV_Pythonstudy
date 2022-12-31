#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import os
import numpy as np

dirname = 'face_images'

cap = cv2.VideoCapture(0)

def mosaic(img, alpha):
  w = img.shape[1]
  h = img.shape[0]
 
  img = cv2.resize(img, (int(w*alpha), int(h*alpha)))
  img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)
  return img 

cascade_filepath = "/home/chikara/test/OpenCV_Pythonstudy/mosaic/data/haarcascades/haarcascade_frontalface_alt.xml"
FaceCascade = cv2.CascadeClassifier(cascade_filepath)

count = 0

while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  Face = FaceCascade.detectMultiScale(gray,1.1,3,minSize=(100,100))
  if not os.path.exists(dirname):
    os.mkdir(dirname)

  if len(Face) > 0:
       for (x, y, w, h) in Face:
         frame[y:y+h, x:x+w] = mosaic(frame[y:y+h, x:x+w], 0.07)


  for (x,y,w,h) in Face:
    count += 1
    count_padded = '%05d' % count
    #cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),thickness=2)
    write_file = count_padded + ".png"
    cv2.imwrite(os.path.join(dirname, write_file), frame)

  cv2.imshow('result', frame)

  key = cv2.waitKey(1)
  if key != -1:
    break

cv2.destroyAllWindows()
cap.release()
