import numpy as np
import cv2
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src = cv2.imread('images/lenna_noise.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.medianBlur(src, 5)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()