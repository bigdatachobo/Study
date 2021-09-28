import cv2
import numpy as np

#from Common.utils import put_string


def put_string(frame, text, pt, value, color=(120, 200, 90)):             # 문자열 출력 함수 - 그림자 효과
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)  # 그림자 효과
    cv2.putText(frame, text, pt, font, 0.7, (120, 200, 90), 2)  # 글자 적기

def zoom_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_ZOOM, value) # 줌 설정 

def focus_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_FOCUS, value)

capture = cv2.VideoCapture(0)	
							# 0번 카메라 연결
if capture.isOpened() is None: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)      # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)     # 카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)          # 오토포커싱 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)       # 프레임 밝기 초기화

title = "Change Camera Properties"              # 윈도우 이름 지정
cv2.namedWindow(title)                          # 윈도우 생성 - 반드시 생성 해야함
cv2.createTrackbar("zoom" , title, 0, 10, zoom_bar)
cv2.createTrackbar("focus", title, 0, 40, focus_bar)

while True:
    ret, frame = capture.read()                 # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    zoom = int(capture.get(cv2.CAP_PROP_ZOOM))
    focus = int(capture.get(cv2.CAP_PROP_FOCUS))
    put_string(frame, "zoom : " , (10, 240), zoom)   # 줌 값 표시
    put_string(frame, "focus : ", (10, 270), focus)    # 초점 값 표시 
    cv2.imshow(title, frame)

capture.release()