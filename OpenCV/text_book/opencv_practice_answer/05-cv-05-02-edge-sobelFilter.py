import sys
import numpy as np
import cv2

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, -1, 2, 0, delta=128)
dy = cv2.Sobel(src, -1, 0, 1, delta=128)
dxy = cv2.Sobel(src, -1, 1, 0 , scale=200, delta=128)

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.imshow('dxy', dxy)
cv2.waitKey()

cv2.destroyAllWindows()