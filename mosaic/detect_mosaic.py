#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np

#動画の読み込み
cap = cv2.VideoCapture(0)

def mozaiku(img, alpha):
  #画像の形状を取得
  w = img.shape[1]
  h = img.shape[0]

  #サイズ加工(最近傍補間)
  img = cv2.resize(img, (int(w*alpha), int(h*alpha)))
  img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)
  print(img)
  return img

#映らない場合の処理
if cap.isOpened() is False:
  sys.exit("can not open camera")

#画像モデルの読み込み
faceCascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalface_alt2.xml")

#動画終了まで繰り返し
while True:
  #動画読み込み
  ret, frame = cap.read()
  #グレースケールの取得
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #顔の検出
  face = faceCascade.detectMultiScale(gray,1.1,3,minSize=(100,100))
  #顔を検出するとモザイク
  if len(face) > 0:
       for (x, y, w, h) in face:
         frame[y:y+h, x:x+w] = mozaiku(frame[y:y+h, x:x+w], 0.07)
  #動画を表示
  cv2.imshow('video', frame)
  #キーが押されると閉じる
  key = cv2.waitKey(1)
  if key != -1:
    break

cap.release()
cv2.destroyAllWindows()
