import cv2
import numpy as np
import os
import random
import xml.etree.ElementTree as ET


#  将小目标贴到底板图上
srcdir = r'/home/yaobo/background/'
objdir = r'/home/yaobo/e12'
savedir = '/home/yaobo/dataSets/e12/'
xmldir = '/home/yaobo/dataSets/e12/'

srcname = os.listdir(srcdir)
srcname.sort()
print(len(srcname))
objname = os.listdir(objdir)

count = 0
for srcfile in srcname:
    srcpath = os.path.join(srcdir, srcfile)
    src = cv2.imread(srcpath)
    t = 3 #random.randint(3, 5)

    root = ET.Element("annotation")
    tree = ET.ElementTree(root)

    folder = ET.Element("folder")
    folder.text = "e12"    # 标签名
    root.append(folder)

    filename = ET.Element("filename")
    filename.text = srcfile
    root.append(filename)

    path = ET.Element("path")
    path.text = "default"
    root.append(path)

    source = ET.Element("source")
    root.append(source)
    database = ET.Element("database")
    database.text = "Unknown"
    source.append(database)

    size = ET.Element("size")
    root.append(size)

    width = ET.Element("width")
    width.text = "4000"
    size.append(width)

    height = ET.Element("height")
    height.text = "3000"
    size.append(height)

    depth = ET.Element("depth")
    depth.text = "3"
    size.append(depth)

    segmented = ET.Element("segmented")
    segmented.text = "0"
    root.append(segmented)

    try:
        for time in range(t):
            i = random.randint(0, len(objname)-1)
            objfile = objname[i]
            objpath = os.path.join(objdir, objfile)
            obj = cv2.imread(objpath)

            obj_h = obj.shape[0]
            obj_w = obj.shape[1]

            src_w = random.randint(200, 400) + time*800
            src_h = random.randint(200, 400) + time*800

            src[src_h:src_h+obj_h, src_w:src_w+obj_w] = obj

            object = ET.Element("object")
            root.append(object)

            name = ET.Element("name")
            name.text = "e12"          # 标签名
            object.append(name)

            pose = ET.Element("pose")
            pose.text = "Unspecified"
            object.append(pose)

            truncated = ET.Element('truncated')
            truncated.text = '0'
            object.append(truncated)

            difficult = ET.Element('difficult')
            difficult.text = '0'
            object.append(difficult)

            bndbox = ET.Element("bndbox")
            object.append(bndbox)

            xmin = ET.Element("xmin")
            xmin.text = str(src_w)
            bndbox.append(xmin)

            ymin = ET.Element("ymin")
            ymin.text = str(src_h)
            bndbox.append(ymin)

            xmax = ET.Element("xmax")
            xmax.text = str(src_w + obj_w)
            bndbox.append(xmax)

            ymax = ET.Element("ymax")
            ymax.text = str(src_h + obj_h)
            bndbox.append(ymax)
    except:
        print("越界")
        count += 1
        continue
    saveapth = savedir + srcfile
    cv2.imwrite(saveapth, src, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    xmlfile = srcfile.replace('jpg', 'xml')
    savexmlpath = xmldir + xmlfile
    tree.write(savexmlpath)

    print('{}已完成'.format(srcfile))
print('成功完成：'+str(len(srcname)-count)+'个')