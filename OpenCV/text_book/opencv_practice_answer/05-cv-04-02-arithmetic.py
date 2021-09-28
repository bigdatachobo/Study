import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


src1 = cv2.imread('images/lenna_gray.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('images/square.bmp', cv2.IMREAD_GRAYSCALE)
# src1  = cv2.imread('images/airplane.bmp', cv2.IMREAD_COLOR)
# src2  = cv2.imread('images/field.bmp', cv2.IMREAD_COLOR)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

#원본 색상을 표현하기 위해서 plt에서는 cv2.cvtColor를 적용해 줘야한다.
# src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addWeighted')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
plt.show()
