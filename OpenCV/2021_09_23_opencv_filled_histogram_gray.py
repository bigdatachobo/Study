import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)
    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)
    return imgHist

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)

cv2.imshow('src', src)
cv2.imshow('histImg', histImg)
cv2.waitKey()
cv2.destroyAllWindows()