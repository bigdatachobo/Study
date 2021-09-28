import cv2
import sys
import math
import cv2 as cv
import numpy as np

cap = cv2.VideoCapture("videos/road5.mp4")

while (True):
    ret, src = cap.read()

    src = cv2.resize(src, (640, 360))

    edges = cv.Canny(src, 50, 200, None, 3)
    dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    dstP = np.copy(dst)
    lines = cv.HoughLines(edges, 1, np.pi / 180, 150, None, 0, 0)

    # edges = cv2.Canny(src, 50, 150)
    # dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    # print(edges.shape)
    # lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160,
    #                         minLineLength=50, maxLineGap=5)
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv.line(dst, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)
            # pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
            # pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
            # cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

    linesP = cv.HoughLinesP(edges, 1, np.pi/180, 50, None, 
                                    minLineLength=50, maxLineGap=5)
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(dstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv.LINE_AA)

    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", dst)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", dstP)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()