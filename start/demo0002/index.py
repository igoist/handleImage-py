#!/usr/bin/python
#coding=utf-8

import PIL.Image as Image
import scipy.misc as misc
import numpy as np

import os
import configparser

config = configparser.ConfigParser()
config.read('../config.conf')
path_img = config.get('info', 'path_img')


def convert_3d(r, mode='dark'):
  _lamda = 0
  if mode == 'dark':
    _lamda = 0.67
  if mode == 'light':
    _lamda = 1.5
  s = np.empty(r.shape, dtype=np.uint8)
  for j in range(r.shape[0]):
    for i in range(r.shape[1]):
      s[j][i] = (r[j][i] / 255) ** _lamda * 255
  return s


# img = Image.open(os.path.join(path_img, 'dark00.jpg'))
img = Image.open(os.path.join(path_img, 'light00.jpg'))
img_matrix = misc.fromimage(img)
# img_converted_matrix = convert_3d(img_matrix, 'dark')
img_converted_matrix = convert_3d(img_matrix, 'light')
img_converted = Image.fromarray(img_converted_matrix)
img_converted.show()