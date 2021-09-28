import numpy as np
import cv2

image = np.zeros((200,300), np.uint8)
image.fill(255)               # image[:] = 255, 흰색지정

title1, title2 = 'NORMAL', 'AUTOSIZE'
cv2.namedWindow(title1, cv2.WINDOW_NORMAL)   #영상 크기를 창 크기에 맞게 지정
cv2.namedWindow(title2, cv2.WINDOW_AUTOSIZE) #창 크기를 영상 크기에 맞게 변경

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300)  
cv2.resizeWindow(title2, 400, 300)  
cv2.waitKey()
cv2.destroyAllWindows()
