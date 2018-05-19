#!/usr/bin/python
#coding=utf-8

import matplotlib.pyplot as plot
import PIL.Image as Image
import scipy.misc
import numpy as np

import os
import configparser


config = configparser.ConfigParser()
config.read('../config.conf')
path_img = config.get('info', 'path_img')

def convert_2d(r):
  x = np.zeros([256])
  for i in range(r.shape[0]):
    for j in range(r.shape[1]):
      x[r[i][j]] += 1
  x = x / r.size

  sum_x = np.zeros([256])
  for i, _ in enumerate(x):
    sum_x[i] = sum(x[:i])

  s = np.empty(r.shape, dtype=np.uint8)
  for i in range(r.shape[0]):
    for j in range(r.shape[1]):
      s[i][j] = 255 * sum_x[r[i][j]]
  return s


img = Image.open(os.path.join(path_img, 'dark01.png'))
img = img.convert('L')
img_matrix = scipy.misc.fromimage(img)

# old img
plot.hist(img_matrix.reshape([img_matrix.size]), 256, density=1)
plot.show()

img_converted_matrix = convert_2d(img_matrix)

# new one
plot.hist(img_converted_matrix.reshape([img_converted_matrix.size]), 256, density=1)
plot.show()

img_converted = Image.fromarray(img_converted_matrix)
img_converted.show()