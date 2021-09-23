import numpy as np
import cv2
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)
# sigma 값을 이용하여 가우시안 필터링
for sigma in range(1,7):
    dst = cv2.GaussianBlur(src, (0, 0), sigma)
    desc = f'sigma = {sigma}'
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
    1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()