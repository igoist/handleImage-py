#!/usr/bin/python
#coding=utf-8

import matplotlib.pyplot as plot
import numpy as np

import PIL.Image as Image
import PIL.ImageFilter as Filter
import scipy.misc

import os
import configparser


config = configparser.ConfigParser()
config.read('../config.conf')
path_img = config.get('info', 'path_img')

# 生成均值为 0, 标准差为 64 的正态分布数据
# data = np.random.normal(0, 64, 1024 * 8)

# 在 plot 中画出直方图
# plot.hist(data, 256, normed=1)
# plot.show()


# 为图像添加高斯白噪声
# 注意到添加完噪声的图像, 像素值可能低于 0 或高于 255
# 此时应该对转换后的图像做一次对比拉伸
def convert_2d(r):
  s = r + np.random.normal(0, 64, r.shape)
  if np.min(s) >= 0 and np.max(s) <= 255:
    return s
  s = s - np.full(s.shape, np.min(s))
  s = s * 255 / np.max(s)
  s = s.astype(np.uint8)
  return s

def convert_3d(r):
  s_dsplit = []
  for d in range(r.shape[2]):
    rr = r[:, :, d]
    ss = convert_2d(rr)
    s_dsplit.append(ss)
  s = np.dstack(s_dsplit)
  return s

# 加噪
img = Image.open(os.path.join(path_img, 'girl.jpg'))
img = img.convert('RGB')
img_matrix = scipy.misc.fromimage(img)
img_converted_matrix = convert_3d(img_matrix)
img_converted = Image.fromarray(img_converted_matrix)
# img_converted.show()


# 去噪
# 之前有个误区，其实应该是去噪（多次加噪）后跟原图几乎接近的意思
# img2 = img_converted.convert('RGB')
# img2 = Image.open(os.path.join(path_img, 'girl02.jpg'))
# img2 = img2.convert('RGB')
img_matrix = scipy.misc.fromimage(img)
k = 128

img_converted_matrix = np.zeros(img_matrix.shape)
for i in range(k):
  img_converted_matrix += convert_3d(img_matrix)

img_converted_matrix = img_converted_matrix / k
img_converted_matrix = img_converted_matrix - np.full(img_converted_matrix.shape, np.min(img_converted_matrix))
img_converted_matrix = img_converted_matrix * 255 / np.max(img_converted_matrix)
img_converted_matrix = img_converted_matrix.astype(np.uint8)

img_converted = Image.fromarray(img_converted_matrix)
img_converted.show()