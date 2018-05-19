#!/usr/bin/python
#coding=utf-8

import PIL.Image
import scipy.misc
import numpy as np

import os
import configparser

config = configparser.ConfigParser()
config.read('../config.conf')
path_img = config.get('info', 'path_img')


def convert_2d(r):
  rmin = np.min(r)
  rmax = np.max(r)
  # print(rmin, rmax)
  if rmin == rmax:
    return r
  s = np.empty(r.shape, dtype=np.uint8)
  for j in range(r.shape[0]):
    for i in range(r.shape[1]):
      s[j][i] = (r[j][i] - rmin) / (rmax - rmin) * 255
      # s[j][i] = 170 + (r[j][i] - rmin) / (rmax - rmin) * 65
      # print(s[j][i])
  return s

def convert_3d(r):
  s_dsplit = []
  for d in range(r.shape[2]):
    rr = r[:, :, d]
    ss = convert_2d(rr)
    s_dsplit.append(ss)
  s = np.dstack(s_dsplit)
  return s


# img = PIL.Image.open(os.path.join(path_img, 'dark01.png'))
img = PIL.Image.open(os.path.join(path_img, 'dark03.jpeg'))
img_matrix = scipy.misc.fromimage(img)
img_converted_matrix = convert_3d(img_matrix)
img_converted = PIL.Image.fromarray(img_converted_matrix)
img.show()