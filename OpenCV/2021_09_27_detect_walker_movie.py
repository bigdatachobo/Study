import random
import numpy as np
import cv2
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

def rand_color():
    return  tuple(sorted([i for i in range(256)] * 3, key=lambda x:random.random())[:3])

# 동영상 불러오기
cap = cv2.VideoCapture('videos/india.mp4')
# 보행자 검출을 위한 HOG 기술자 설정
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
while True:
    ret, frame = cap.read()
    # 매 프레임마다 보행자 검출
    detected, _ = hog.detectMultiScale(frame)
    # 검출 결과 화면 표시
    for (x, y, w, h) in detected:
        c = rand_color()
        cv2.rectangle(frame, (x, y, w, h), c, 3)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()