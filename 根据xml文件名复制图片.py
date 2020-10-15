# -*- coding: UTF-8 -*-
from PIL import Image
import os
from shutil import copyfile
data = []
xmlPath = "C:\\Users\\cc\\Desktop\\fsdownload\\Annotations\\"     # xml路径
SrcPath = "C:\\Users\\cc\\Desktop\\fsdownload\\JPEGImages\\"     #  原图片路径
DstPath = "C:\\Users\\cc\\Desktop\\fsdownload\\Annotations1\\"     #  保存路径
Srcs = os.listdir(SrcPath)

for Src in Srcs:
    index = os.path.splitext(Src)[0]
    #print(index)
    imagename = index + '.xml'
    copyfile(xmlPath + imagename, DstPath + imagename)
    # im = Image.open("C:\\Users\\cc\\Desktop\\1\\{}".format(a[:-1]))     # 将换行符“\n”除去
    # im.save("C:\\Users\\cc\\Desktop\\2\\{}".format(a[:-1]))
