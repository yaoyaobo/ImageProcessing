#-*-encoding = utf-8 -*-
import os
import random
import shutil

def movefile(fileDir):
    pathDir = os.listdir(fileDir)
    filenumber = len(pathDir)
    rate = 0.1
    picknumber = int(filenumber * rate)
    sample = random.sample(pathDir,picknumber)
    print(sample)
    for name in sample:
        shutil.move(fileDir+name,tarDir+name)

if __name__ == '__main_':
    fileDir = "/home/yaobo/DBTNet-master/data/imagenet/train/0/"    #源图片文件夹路径
    tarDir = "/home/yaobo/DBTNet-master/data/imagenet/val/0/"#目标图片文件夹路径
    movefile(fileDir)
