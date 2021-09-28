import numpy as np
import cv2

# 부분 영상 추출
img1 = cv2.imread('images\HappyFish.png')

img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱
img3 = img1[40:120, 30:150].copy()

img2.fill(0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)    #검은색
#cv2.imshow('img3', img3)   #부분이미지
cv2.waitKey()
cv2.destroyAllWindows()
