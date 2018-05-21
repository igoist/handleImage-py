#!/usr/bin/python
#coding=utf-8

import PIL.Image as Image
import PIL.ImageFilter as Filter
import scipy.misc
import numpy as np

import os
import configparser


config = configparser.ConfigParser()
config.read('../config.conf')
path_img = config.get('info', 'path_img')

def convert_2d(r, h):
  # 矩阵减法
  s = r - h
  if np.min(s) >= 0 and np.max(s) <= 255:
    return s
  # 线性拉伸
  s = s - np.full(s.shape, np.min(s))
  s = s * 255 / np.max(s)
  s = s.astype(np.uint8)
  return s

def convert_3d(r, h):
  s_dsplit = []
  for d in range(r.shape[2]):
    rr = r[:, :, d]
    hh = h[:, :, d]
    ss = convert_2d(rr, hh)
    s_dsplit.append(ss)
  s = np.dstack(s_dsplit)
  return s

img = Image.open(os.path.join(path_img, 'girl.jpg'))
img = img.convert('RGB')
img_matrix = scipy.misc.fromimage(img)
# use gaussian blur as example
img_converted = img.filter(Filter.GaussianBlur(radius=2))
img_converted_matrix = scipy.misc.fromimage(img_converted)
img_sub_matrix = convert_3d(img_matrix, img_converted_matrix)
img_sub = Image.fromarray(img_sub_matrix)
img_sub.show()
