import numpy as np
import cv2
import sys
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src = cv2.imread('images/rose.bmp') # src.shape=(320, 480, 3)

dst1 = cv2.resize(src, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# 차이점 알아보기 위해 확대 변환
dst1_e = cv2.resize(dst1, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC )
dst2_e = cv2.resize(dst2, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC )

cv2.imshow('src', src)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.imshow('dst1_e', dst1_e)
cv2.imshow('dst2_e', dst2_e)

cv2.waitKey()
cv2.destroyAllWindows()