import sys
import cv2
import numpy as np

# 마스크 영상을 이용한 영상 합성
src  = cv2.imread('images/airplane.bmp', cv2.IMREAD_COLOR)
mask = np.zeros_like(src)
cv2.circle(mask, (380,210), 100, (255,255,255), -1)
# 마스크-원: cv2.circle(대상이미지, (원점x, 원점y), 반지름, (색상), 채우기)

masked = cv2.bitwise_and(src, mask)

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('masked', masked)
cv2.waitKey()
cv2.destroyAllWindows()