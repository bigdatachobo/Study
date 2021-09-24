import math
import numpy as np
import cv2
import sys
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

def detect_line(frame):
    edges = cv2.Canny(frame, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160,
                            minLineLength=100, 
                            maxLineGap=3)
    dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    if lines is not None:
        for i in range(lines.shape[0]):
            pt1 = (lines[i][0][0], lines[i][0][1]) # 시작점 좌표
            pt2 = (lines[i][0][2], lines[i][0][3]) # 끝점 좌표
            cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)
    return dst

cap = cv2.VideoCapture('videos/road.mp4')
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame',frame)
        cv2.imshow('dst', detect_line(frame))

        if cv2.waitKey(10) == 27:
            break
    else:
        break

cv2.destroyAllWindows()