# -*-coding=utf-8 -*-

import os
import cv2
import xlwt
from xml.etree.ElementTree import ElementTree, Element
#　统计xmｌ中各个目标的数量
data_root_path = '/home/yaobo/VOC2020/'


def modify_xml(data_root_path):
    Annotation_path = os.path.join(data_root_path, 'Annotations')
    Annotations = os.listdir(Annotation_path)
    a1_num = 0
    a2_num = 0
    a3_num = 0
    a4_num = 0
    a10_num = 0
    a12_num = 0
    a21_num = 0
    a22_num = 0
    a41_num = 0
    a92_num = 0
    a102_num = 0
    a122_num = 0
    b13_num = 0
    b28_num = 0
    c21_num = 0
    e12_num = 0
    e40_num = 0
    e90_num = 0
    e120_num = 0
    g21_num = 0
    for i, Annotation in enumerate(Annotations):
        if os.path.splitext(Annotation)[1] == '.xml':
            xml_path = os.path.join(Annotation_path, Annotation)
            tree = ElementTree()
            tree.parse(xml_path)
            # 修改floder
            # floder = tree.find('folder')
            # floder.text = "voc2020"

            # 修改filename
            # filename = tree.find('filename')
            # filename.text = os.path.splitext(Annotaton)[0] + '.jpg'
            # 修改 size
            root = tree.getroot()
            # size = root.find('size')
            # size.find('width').text = str(4000)
            # size.find('height').text = str(3000)

            # path = tree.find('path')
            # path.text = root.remove(path)

            for object in root.findall('object'):
                name = object.find('name').text
                if name == 'a1':
                    a1_num += 1
                if name == 'a2':
                    a2_num += 1
                if name == 'a3':
                    a3_num += 1
                if name == 'a4':
                    a4_num += 1
                if name == 'a10':
                    a10_num += 1
                if name == 'a12':
                    a12_num += 1
                if name == 'a21':
                    a21_num += 1
                if name == 'a22':
                    a22_num += 1
                if name == 'a41':
                    a41_num += 1
                if name == 'a92':
                    a92_num += 1
                if name == 'a102':
                    a102_num += 1
                if name == 'a122':
                    a122_num += 1
                if name == 'b13':
                    b13_num += 1
                if name == 'b28':
                    b28_num += 1
                if name == 'c21':
                    c21_num += 1
                if name == 'e12':
                    e12_num += 1
                if name == 'e40':
                    e40_num += 1
                if name == 'e90':
                    e90_num += 1
                if name == 'e120':
                    e120_num += 1
                if name == 'g21':
                    g21_num += 1
            # new_xml_path = os.path.join(data_root_path, Annotation)
            # tree.write(new_xml_path, encoding='utf-8')
    print("蝼蛄a1_num:" + str(a1_num))
    print("二化螟a2_num:" + str(a2_num))
    print("铜绿丽金龟a3_num:" + str(a3_num))
    print("草地螟a4_num:" + str(a4_num))
    print("黄金镰翅野螟a10_num:" + str(a10_num))
    print("稻纵卷叶螟a12_num:" + str(a12_num))
    print("大螟a21_num:" + str(a21_num))
    print("玉米螟a22_num:" + str(a22_num))
    print("槐尺蛾a41_num:" + str(a41_num))
    print("a92_num:" + str(a92_num))
    print("棉铃虫a102_num:" + str(a102_num))
    print("粘虫a122_num:" + str(a122_num))
    print("灰胸突鳃金龟b13_num:" + str(b13_num))
    print("大黑鳃金龟b28_num:" + str(b28_num))
    print("黄足猎蝽c21_num:" + str(c21_num))
    print("烟青虫e12_num:" + str(e12_num))
    print("杨雪毒蛾e40_num:" + str(e40_num))
    print("榆黄足毒蛾e90_num:" + str(e90_num))
    print("橄榄绿尾尺蛾e120_num:" + str(e120_num))
    print("蟋蟀g21_num:" + str(g21_num))
    print('finished!')


if __name__ == '__main__':
    modify_xml(data_root_path)
