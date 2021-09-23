import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src = cv2.imread('images/lenna.bmp')
colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)
for (bgr, color) in zip(bgr_planes, colors):
    hist = cv2.calcHist([bgr], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
cv2.imshow('src', src)
cv2.waitKey(1)
plt.show()