import numpy as np
import cv2
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

def onTrackbar(th):
    rep_edge = cv2.Canny(rep_gray, th, th*3, 5) # 캐니 에지 검출
    h, w = src.shape[:2]
    cv2.rectangle(rep_edge, (0, 0, w, h), 255, -1) # 흰색 사각형 그리기
    color_edge = cv2.bitwise_and(rep_img, rep_img, mask=rep_edge) #scr2에 마스크 적용
    cv2.imshow("color edge", color_edge)

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_COLOR)
th = 50
rep_img = cv2.repeat(src, 1, 2) # 가로 반복 복사
rep_gray = cv2.cvtColor(rep_img, cv2.COLOR_BGR2GRAY) # 명암도 영상 변환
cv2.namedWindow("color edge", cv2.WINDOW_NORMAL) # 윈도우 생성
cv2.createTrackbar("Canny th", "color edge", th, 100, onTrackbar) # 콜백 함수 등록
onTrackbar(th) # 콜백 함수 첫 실행
cv2.waitKey()
cv2.destroyAllWindows()