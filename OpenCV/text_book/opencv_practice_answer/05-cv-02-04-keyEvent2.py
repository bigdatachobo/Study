#키보드 이벤트
import cv2
import sys

img = cv2.imread('images/cat.jpg') 
cv2.imshow('image', img)

while True :
    key = cv2.waitKey()
    if key == 27 :    # ESC키
        break
    elif key == ord('s') or key == ord('S'):
        print('original-------',img)
        img = ~img
        print('Not-------',img)
        cv2.imshow('image', img)

cv2.destroyAllWindows()
