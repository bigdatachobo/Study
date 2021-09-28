import numpy as np
import cv2

image = cv2.imread('images/cat.jpg')
h, w = image.shape[0:2]
#print(h, w)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE) 

cv2.imshow('image', image)   # 위치를 resizeWindow보다 먼저 지정해야된다.
cv2.moveWindow('image', 300, 300)
cv2.resizeWindow('image', w+100, h+100 ) 

cv2.waitKey()
cv2.destroyAllWindows()
