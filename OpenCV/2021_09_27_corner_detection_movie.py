import cv2
import sys
import numpy as np
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

cap = cv2.VideoCapture('videos/road.mp4')
# 두 영상에서 특징점 검출 & 출력(KAZE, AKAZE, ORB 등)
feature = cv2.KAZE_create()
feature2 = cv2.AKAZE_create()
# feature = cv2.ORB_create()
while True:
    key = cv2.waitKey(1)
    ret,frame = cap.read()
    if ret:
        kp1 = feature.detect(frame)
        kp2 = feature2.detect(frame)
        # 검출된 특징점 출력 영상 생성
        dst1 = cv2.drawKeypoints(frame, kp1, None,
        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        dst2 = cv2.drawKeypoints(frame, kp2, None,
        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('dst1', dst1)
        cv2.imshow('dst2', dst2)

        if key == 27:
            break
    else:
        break
cv2.destroyAllWindows()

#특징점 검출 예제
# of kp1: 666
# of kp2: 515
