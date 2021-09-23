import numpy as np
import cv2
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src = cv2.imread('images/lenna_noise.bmp', cv2.IMREAD_GRAYSCALE)
bifi_src = cv2.GaussianBlur(src,(0,0),3)

dx = cv2.Sobel(bifi_src, -1, 1, 0, delta=128)
dy = cv2.Sobel(bifi_src, -1, 0, 1, delta=128)

cv2.imshow('src', bifi_src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)

cv2.waitKey()
cv2.destroyAllWindows()
