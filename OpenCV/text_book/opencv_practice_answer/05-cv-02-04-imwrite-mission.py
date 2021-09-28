#영상파일 출력하기
import cv2
import sys

img = cv2.imread('images/cat.jpg')
img1 = cv2.imread('images/cat.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imwrite('images/cat_gray.jpg', img1, [cv2.IMWRITE_JPEG_QUALITY, 90])

print(f'img---{img.shape}\n',img)
print(f'img1---{img1.shape}\n',img1)

if img2 is None:
    print('Image save failed!')
    sys.exit()

#cv2.namedWindow('image')
cv2.imshow('image1', img1)
img2 = cv2.imread('images/cat_gray.jpg')
print(f'img2---{img2.shape}\n',img2)
cv2.imshow('image2', img2)
cv2.waitKey()

cv2.destroyAllWindows()
