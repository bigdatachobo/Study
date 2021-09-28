import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

# 컬러 영상의 히스토그램
src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
hist.flatten()
plt.plot(hist, color='gray')

cv2.imshow('src', src)
cv2.waitKey()

plt.show()

cv2.destroyAllWindows()
