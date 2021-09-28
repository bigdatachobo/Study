import sys
import numpy as np
import cv2
import math

src = cv2.imread('images/parasol.jpg')  
print(src.shape)
if src is None:
    print('Image load failed!')
    sys.exit()

cp = (src.shape[1] / 2, src.shape[0] / 2)
rot = cv2.getRotationMatrix2D(cp, 20, 1)
print(f'h:{src.shape[0]}, w:{src.shape[1]}')
print(f'cp: {cp}')
print(f'rot: {rot}')

dst = cv2.warpAffine(src, rot, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
