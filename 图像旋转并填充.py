# -*- coding:utf-8 -*-
import cv2
import numpy as np

def rotate(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH), borderValue=(154, 152, 151))
if __name__ == '__main__':
    image = cv2.imread("./dzjym.jpg")
    print(image.shape)
    rotate_45 = rotate(image, 45)
    rotate_90 = rotate(image, 90)
    rotate_135 = rotate(image, 135)
    rotate_180 = rotate(image, 180)
    rotate_225 = rotate(image, 225)
    rotate_270 = rotate(image, 270)
    rotate_315 = rotate(image, 315)

    cv2.imwrite("45.jpg", rotate_45)
    cv2.imwrite("90.jpg", rotate_90)
    cv2.imwrite("135.jpg", rotate_135)
    cv2.imwrite("180.jpg", rotate_180)
    cv2.imwrite("225.jpg", rotate_225)
    cv2.imwrite("270.jpg", rotate_270)
    cv2.imwrite("315.jpg", rotate_315)

