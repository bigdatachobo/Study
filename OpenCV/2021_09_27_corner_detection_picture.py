import cv2
import sys
import numpy as np
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src1 = cv2.imread('images/hough2.jpg', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('images/hough.jpg', cv2.IMREAD_GRAYSCALE)

# 두 영상에서 특징점 검출 & 출력(KAZE, AKAZE, ORB 등)
feature = cv2.KAZE_create()
# feature = cv2.AKAZE_create()
# feature = cv2.ORB_create()
kp1 = feature.detect(src1)
kp2 = feature.detect(src2)
# 검출된 특징점 출력 영상 생성
dst1 = cv2.drawKeypoints(src1, kp1, None,
flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst2 = cv2.drawKeypoints(src2, kp2, None,
flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

#특징점 검출 예제
# of kp1: 666
# of kp2: 515
