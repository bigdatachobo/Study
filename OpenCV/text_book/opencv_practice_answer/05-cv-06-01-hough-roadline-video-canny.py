import cv2
import sys
import math
import cv2 as cv
import numpy as np

cap = cv2.VideoCapture("videos/road5.mp4")

while (True):
    ret, src = cap.read()

    if not ret:
        print('can not read!')
        sys.exit()

    src = cv2.resize(src, (640, 360))
    edges = cv2.Canny(src, 50, 150)  
    dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    lines = cv.HoughLinesP(edges, 1, np.pi / 180., 160,  
                                minLineLength=100, maxLineGap=5)
    if lines is not None:
        for i in range(0, len(lines)):
            l = lines[i][0]
            cv.line(dst, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv.LINE_AA)

    cv.imshow("Source", src)        
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", dst)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()