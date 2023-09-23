#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_src = cv2.imread("/home/chikara/Pictures/lena.jpeg")

def parse_pgm(fd):
  w = 0
  h = 0
  lim = 0
  lines = 0
  count = 0
  wFlag = True
  val = np.array([])
  fd = open(img_path, 'rb')
  ch = fd.read(1)
  
  return w. h. lim

def simple_demosaicing(img_src)
