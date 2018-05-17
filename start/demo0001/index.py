#!/usr/bin/python
#coding=utf-8

import PIL.Image
import PIL.ImageStat

import os
import configparser

config = configparser.ConfigParser()
config.read('../config.conf')
path_img = config.get('info', 'path_img')

img = PIL.Image.open(os.path.join(path_img, 'girl.jpg'))
mean = PIL.ImageStat.Stat(img).mean
print(mean)

# print(os.path.join(path_img, 'girl.jpg'))

# dir = os.path.dirname(__file__)
# print(dir)
# print(os.path.join(dir, 'index.js'))

# print(type(path_img))
# print(type(dir))

