import sys
import numpy as np
import cv2

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('src', src)

# 1단계: 가우시안 필터 적용
gaus_img = cv2.GaussianBlur(src, (5, 5), 0.3)
cv2.imshow('src', gaus_img)

# 2단계: 그래디언트 계산 적용
dx = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 1, 0, 3) # x방향, kernel size = 3
dy = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 0, 1, 3) # y방향, kernel size = 3
mag = cv2.magnitude(dx, dy)
sobel_img = np.clip(mag, 0, 255).astype(np.uint8) # Magnitude의 발산을 막아주기 위해 필수
_, sobel_img = cv2.threshold(sobel_img, 120, 255, cv2.THRESH_BINARY)
cv2.imshow('sobel_img', sobel_img)

# 3단계: 비최대 억제
def nonmax_suppression(sobel, direct):
    rows, cols = sobel.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # 관심 영역 참조 통해 이웃 화소 가져오기
            values = sobel[i-1:i+2, j-1:j+2].flatten()
            first = [3, 0, 1, 2]
            id = first[direct[i, j]]
            v1, v2 = values[id], values[8-id]
            dst[i, j] = sobel[i, j] if (v1 < sobel[i, j] > v2) else 0
    return dst
    
directs = cv2.phase(dx, dx) / (np.pi/4)
directs = directs.astype(int) % 4
max_sobel = nonmax_suppression(sobel_img, directs)
cv2.imshow('max_sobel', max_sobel)

cv2.waitKey()
cv2.destroyAllWindows()