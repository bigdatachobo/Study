import numpy as np
import cv2

def calc_histo(image, hsize, ranges=[0, 256]):  # 행렬 원소의 1차원 히스토그램 계산
    hist = np.zeros((hsize, 1), np.float32)  # 히스토그램 누적 행렬
    gap = ranges[1] / hsize  # 계급 간격

    for i in range(image.shape[0]):  # 2차원 행렬 순회 방식
        for j in range(image.shape[1]):
            idx = int(image.item(i,j) / gap)
            hist[idx] += 1
    return hist

image = cv2.imread("images/lenna.bmp", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

hsize, ranges = [32], [0, 256]                  # 히스토그램 간격수, 값 범위
gap = ranges[1]/hsize[0]
ranges_gap  = np.arange(0, ranges[1]+1, gap)
print(f'hsize: {hsize}, gap: {gap}')
print(f'ranges_gap: {ranges_gap}')

hist1 = calc_histo(image, hsize[0], ranges)  # User 함수
hist2 = cv2.calcHist([image], [0], None, hsize, ranges)  # OpenCV 함수
hist3, bins = np.histogram(image, ranges_gap )

print("User 함수: \n", hist1.flatten())     # 행렬을 벡터로 변환하여 출력
print("OpenCV 함수: \n", hist2.flatten())   # 행렬을 벡터로 변환하여 출력
print("numpy 함수: \n", hist3)              # 행렬을 벡터로 변환하여 출력

cv2.imshow("image", image)
cv2.waitKey(0)