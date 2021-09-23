import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
cv2.imshow('src', src)
cv2.waitKey(1)
plt.plot(hist)
plt.show()