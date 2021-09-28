#영상파일 출력하기
import cv2
import sys

print('Hello OpenCV', cv2.__version__)

img = cv2.imread('images/cat.jpg') 

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
