# -*- coding:utf-8 -*-
import cv2
import os
images_path = "K:\\fs\\fmb\\"
images = os.listdir(images_path)
for image in images:
    img = cv2.imread(images_path+image)
    h, w  = img.shape[:2]
    (b0, g0, r0) = img[0, 0]  # 读取(0,0)像素，Python中图像像素是按B,G,R顺序存储的
    #print(b0, g0, r0)
    (b1, g1, r1) = img[h-1,0]  # 右上
    #print(b1, g1, r1)
    (b2, g2, r2) = img[0,w-1]  # 左下
    #print(b2, g2, r2)
    (b3, g3, r3) = img[h-1,w-1]  # 读取右下
    #print(b3, g3, r3)
    f = open("C:\\Users\\cc\\Desktop\\111.txt", "w")
    if (b0!=b1 and b1!=b2 and b2!=b3 and b3!=b0):
       print("{}".format(image))
       f.write(image+'\n')


