#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

#動画取得
cap = cv2.VideoCapture(8)

#色の設定
def detect(frame):

  #BGR色空間をHSV色空間に変更
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  #green
  color_min = np.array([30,50,50])
  color_max = np.array([90,255,255])

  #画素を指定してそれ以外を0とする
  mask = cv2.inRange(hsv, color_min, color_max)
  return mask

#撮影開始
while(cap.isOpened()):

  #動画の読み取り
  ret, frame = cap.read()
  
  #サイズを小さくする
  frame = cv2.resize(frame, (int(frame.shape[1]/2), int(frame.shape[1]/2)))

  #グレースケールの取得
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  #色の検出
  mask = detect(frame)

  #白黒映像に赤色追加し、検出を見やすくする
  res = cv2.bitwise_and(gray, mask) 
  ans = cv2.applyColorMap(res, cv2.COLORMAP_DEEPGREEN)

  #緑色の物体の輪郭を抽出
  contours, hierarchy = cv2.findContours(res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  if len(contours) > 0:
    cv2.imwrite('serch.jpg', ans)

  #動画の表示（結果の表示）
  cv2.imshow('Video',frame)
  cv2.imshow('Mask',mask)
  cv2.imshow('Result',ans)

  #キーが打たれると終了
  key = cv2.waitKey(1)
  if key != -1:
    break

cap.release()
cv2.destroyAllWindows()
