import numpy as np
import cv2

# 부분 영상 추출
img1 = cv2.imread('images/cat.jpg')

img2 = img1[0:370, 250:740]  # 고양이 얼굴 numpy.ndarray의 슬라이싱
img3 = img1[0:370, 250:740].copy()

img2.fill(0)

#cv2.imshow('img1', img1)
#cv2.imshow('img2', img2)   #검은색
cv2.imshow('img3', img3)   #부분이미지:고양이 얼굴
cv2.waitKey()
cv2.destroyAllWindows()
