import sys
import numpy as np
import cv2

src = cv2.imread('images/road_evening.jpg', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(src_gray, 50, 150)
print(edges.shape)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160,
                        minLineLength=80, maxLineGap=3)
print(lines.shape)
dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
        pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
