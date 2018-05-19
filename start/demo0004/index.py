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

flat = 6

def convert_2d(r):
  s = np.empty(r.shape, dtype=np.uint8)
  for j in range(r.shape[0]):
    for i in range(r.shape[1]):
      bits = bin(r[j][i])[2:].rjust(8, '0')
      fill = int(bits[-flat - 1])
      s[j][i] = 255 if fill else 0
  return s


img = PIL.Image.open(os.path.join(path_img, 'girl00.jpg'))
img = img.convert('L')
img_matrix = scipy.misc.fromimage(img)
img_converted_matrix = convert_2d(img_matrix)

img_converted = PIL.Image.fromarray(img_converted_matrix)
img_converted.show()