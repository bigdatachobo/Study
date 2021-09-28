import sys
import numpy as np
import cv2


#src = cv2.imread('images/building.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('images/road_evening.jpg', cv2.IMREAD_GRAYSCALE)
print(src.shape)
if src is None:
    print('Image load failed!')
    sys.exit()

edges = cv2.Canny(src, 50, 150)
dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
print(edges.shape)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160,
                        minLineLength=50, maxLineGap=5)
print(lines.shape)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
        pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
