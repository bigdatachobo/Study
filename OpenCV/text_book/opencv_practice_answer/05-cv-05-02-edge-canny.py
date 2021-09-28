import sys
import numpy as np
import cv2

#src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('images/building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.Canny(src, 50, 100)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()