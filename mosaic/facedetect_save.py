#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import os
import numpy as np

#作成するディレクトリ名を宣言
dirname = 'face_images'

#動画の読み込み
cap = cv2.VideoCapture(0)

#モザイクをする関数
def mosaic(img, alpha):
  #画像の形状を取得
  w = img.shape[1]
  h = img.shape[0]
 
  #サイズを加工(最近傍補間)
  img = cv2.resize(img, (int(w*alpha), int(h*alpha)))
  img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)
  return img 

#カスケードパスを宣言
cascade_filepath = "/home/chikara/Python/OpenCV_Pythonstudy/mosaic/data/haarcascades/haarcascade_frontalface_alt.xml"

#画像モデルの読み込み
FaceCascade = cv2.CascadeClassifier(cascade_filepath)

#保存する連番
count = 0

#動画終了まで繰り返す
while True:
  #動画の読み込み
  ret, frame = cap.read()
  #グレースケールを取得
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #人の顔を検出
  Face = FaceCascade.detectMultiScale(gray,1.1,3,minSize=(100,100))
  #指定した名前のディレクトリがなければディレクトリを作成
  if not os.path.exists(dirname):
    os.mkdir(dirname)

  #検出した画素ににモザイク加工
  if len(Face) > 0:
       for (x, y, w, h) in Face:
         frame[y:y+h, x:x+w] = mosaic(frame[y:y+h, x:x+w], 0.07)

  #顔検出をすると画像を保存
  for (x,y,w,h) in Face:
    count += 1
    count_padded = '%05d' % count
    #cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),thickness=2)
    write_file = count_padded + ".png"
    cv2.imwrite(os.path.join(dirname, write_file), frame)

  #動画出力
  cv2.imshow('result', frame)

  #キー入力をすると動画終了
  key = cv2.waitKey(1)
  if key != -1:
    break

cv2.destroyAllWindows()
cap.release()
