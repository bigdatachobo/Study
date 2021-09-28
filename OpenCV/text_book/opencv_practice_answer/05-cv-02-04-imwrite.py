#영상파일 출력하기
import cv2
import sys

print('Hello OpenCV', cv2.__version__)

img1 = cv2.imread('images/cat.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imwrite('images/cat_gray.jpg', img1, [cv2.IMWRITE_JPEG_QUALITY, 90])

if img2 is None:
    print('Image save failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img1)
cv2.waitKey()

cv2.destroyAllWindows()
