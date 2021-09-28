import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

# 컬러 영상의 히스토그램
src = cv2.imread('images/lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    print(p,'-',p,'\n----------\n')
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('src', src)
cv2.waitKey()

plt.show()

cv2.destroyAllWindows()
