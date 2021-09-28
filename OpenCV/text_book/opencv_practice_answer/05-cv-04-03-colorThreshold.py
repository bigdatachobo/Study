import numpy as np
import cv2

def onThreshold(value):
    th[0] = cv2.getTrackbarPos("Hue_th1", "result")
    th[1] = cv2.getTrackbarPos("Hue_th2", "result")

    ##이진화 - 화소 직접 접근 방법
    # result = np.zeros(hue.shape, np.uint8)
    # for i in range(result.shape[0]):
    #     for j in range(result.shape[1]):
    #         if th[0] <= hue[i, j] < th[1] : result[i, j] = 255

    ##이진화 - 넘파이 함수 활용 방식
    # result = np.logical_and(hue < th[1], hue >= th[0])
    # result = result.astype('uint8') *255

    ## OpenCV 이진화 함수 이용 - 상위 값과 하위 값 제거
    _, result = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(result, th[0], 255, cv2.THRESH_BINARY, result)
    cv2.imshow("result", result)


# 컬러 영상 불러오기
BGR_img = cv2.imread('images/candies.png', cv2.IMREAD_COLOR)
if BGR_img is None: raise Exception("영상 파일 읽기 오류")

HSV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2HSV) # 컬러 공간 변환
hue = np.copy(HSV_img[:,:,0])                      # hue 행렬에 색상 채널 복사

th = [50, 100]                                     # 트랙바로 선택할 범위 변수
cv2.namedWindow("result")
cv2.createTrackbar("Hue_th1", "result", th[0], 255, onThreshold)
cv2.createTrackbar("Hue_th2", "result", th[1], 255, onThreshold)
onThreshold(th[0])                                 # 이진화 수행

cv2.imshow("BGR_img", BGR_img)
cv2.waitKey()