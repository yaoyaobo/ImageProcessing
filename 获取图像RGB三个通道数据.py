import os
import numpy as np
import cv2 as cv

image = cv.imread("yao_e12_466.jpg")
print(np.mean((image[:, :, 0])))
print(np.mean(image[:, :, 1]))
print(np.mean(image[:, :, 2]))
