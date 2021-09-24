import numpy as np
import cv2
import sys
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src = cv2.imread('images/parasol.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()
aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32)

h, w = src.shape[:2]

dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()