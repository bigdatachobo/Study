import numpy as np
import cv2
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)

for ksize in (1, 3, 5, 7, 9, 11):
    dst = cv2.blur(src, (ksize, ksize))
    desc = f'Mean: {ksize}x{ksize}'
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
    1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()