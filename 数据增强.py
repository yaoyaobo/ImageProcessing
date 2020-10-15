import os
import numpy as np
import cv2 as cv
import random

#  数据增强
def rotate(img, angle):
    height, width = img.shape[:2]
    matRotate = cv.getRotationMatrix2D((width*0.5, height*0.5), angle, 1)
    dst = cv.warpAffine(img, matRotate, (width, height))
    return dst


def resize_pic(img, scale):
    shape_img = img.shape
    dstHeight = int(shape_img[0]*scale)
    dstWidth = int(shape_img[1]*scale)
    dst = cv.resize(img, (dstWidth, dstHeight))
    return dst


def cut(img, val):
    height, width = img.shape[:2]
    dst = img[int(height*val):height - int(height*val), int(width*val*2):width-int(width*val*2)]
    return dst


def shift(img, val):
    height, width = img.shape[:2]
    dst = np.zeros(img.shape, np.uint8)
    for i in range(height):
        for j in range(width - val):
            dst[i, j + val] = img[i, j]
    return dst


def gassuss_noise(img, mean=0, var=0.002):    #　高斯噪声
    image = np.array(img/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise

    if out.min() < 0:
        low_clip = -1
    else:
        low_clip = 0

    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out * 255)
    return out


#椒盐噪声
def sp_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1-prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


if __name__ == "__main__":
    image_path = '/home/yaobo/1111/1/'
    images = os.listdir(image_path)
    for image in images:
        img = cv.imread(image_path + image)
        new_rotate45 = rotate(img, 45)
        gasuss_noise_image = gassuss_noise(img)
        sp_noise_image = sp_noise(img, 0.01)
        cv.imwrite("/home/yaobo/1111/rotate/{}.jpg".format(image), new_rotate45)
        cv.imwrite("/home/yaobo/1111/gasuss/{}.jpg".format(image), gasuss_noise_image)
        cv.imwrite("/home/yaobo/1111/sp/{}.jpg".format(image), sp_noise_image)