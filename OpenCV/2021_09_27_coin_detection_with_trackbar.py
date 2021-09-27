import cv2
import sys
import numpy as np
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src = cv2.imread('images/coins.jpg')
src = cv2.resize(src,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (0, 0), 1.0)

def on_trackbar(pos):
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')
    circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
    param1=120, param2=th, minRadius=rmin, maxRadius=rmax)
    dst = src.copy()
    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            print(cx, cy, radius)
            cv2.circle(dst, (int(cx), int(cy)), int(radius), (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('img', dst)

cv2.imshow('img', src)
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)
cv2.setTrackbarPos('minRadius', 'img', 10)
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)

cv2.waitKey()
cv2.destroyAllWindows()