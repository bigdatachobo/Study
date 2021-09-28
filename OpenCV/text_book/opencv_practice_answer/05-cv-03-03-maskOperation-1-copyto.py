import sys
import cv2

# 마스크 영상을 이용한 영상 합성
src  = cv2.imread('images/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('images/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst  = cv2.imread('images/field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

cv2.copyTo(src, mask, dst)
# dst[mask > 0] = src[mask > 0]

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()