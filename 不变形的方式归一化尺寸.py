# -*- coding=utf-8 -*-
import os
import cv2
#　将图像以不变形方式放缩到统一尺寸
def resize_image(image, height, width):
    top, bottom, left, right = (0, 0, 0, 0)
    h, w = image.shape[:2]
    longest_edge = max(h, w)
    if h < longest_edge:
        dh = longest_edge-h
        top = dh // 2
        bottom = dh-top
    elif w < longest_edge:
        dw = longest_edge-w
        left = dw // 2
        right = dw - left
    else:
        pass
    mean_color = (154, 155, 152)   # 填充的像素值
    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=mean_color)
    return cv2.resize(constant, (height, width))


def resizeImg(path_name, newpath):
    for dir_item in os.listdir(path_name):
        full_path = path_name + dir_item
        if dir_item.endswith('.jpg'):
            image = cv2.imread(full_path)
            image = resize_image(image, 224, 224)
            cv2.imwrite(newpath + '/'+dir_item, image)
def main():
    image_path = '/home/yaobo/darknet-master/test/finnal/crop/c21/'
    new_path = '/home/yaobo/classifier/resize/c21'
    resizeImg(image_path, new_path)


if __name__ == "__main__":
    main()