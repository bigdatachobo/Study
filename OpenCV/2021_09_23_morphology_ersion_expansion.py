import numpy as np
import cv2
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src = cv2.imread('images/morph.jpg', cv2.IMREAD_GRAYSCALE)
se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

dst1 = cv2.erode(src, se)
dst2 = cv2.dilate(src, None)

cv2.imshow('src', src)
cv2.imshow('erosion', dst1)
cv2.imshow('expansion', dst2)

cv2.waitKey()
cv2.destroyAllWindows()