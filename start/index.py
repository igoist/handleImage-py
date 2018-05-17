#!/usr/bin/python
#coding=utf-8

import scipy.misc
import PIL.Image
import PIL.ImageStat

import os
import configparser

config = configparser.ConfigParser()
config.read('./config.conf')
path_img = config.get('info', 'path_img')


mat = scipy.misc.imread(os.path.join(path_img, 'girl.jpg'))
print(mat.shape)

img = PIL.Image.open(os.path.join(path_img, 'girl.jpg'))
r, g, b = img.split()

# # r.show()
# # g.show()
# # b.show()

# img = PIL.Image.merge('RGB', (b, g, r))
# img.show()

mean = PIL.ImageStat.Stat(img).mean
print(mean)