import numpy as np
import cv2

# 영상 복사
#img1 = cv2.imread('images\HappyFish.jpg')
img1 = cv2.imread('images\HappyFish.png')

img2 = img1
img3 = img1.copy()

#img1.fill(255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

