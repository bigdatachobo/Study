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

    #src = cv2.resize(src, (640, 360))
    h, w, _ = src.shape

    # 1.Canny엣지 추출
    gray_src = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray_src, 50, 150)  

    # 2.ROI 지정
    vertices = np.array([[(200,h-70),(w/2+80, h/2+20), 
                        (w/2+150, h/2+20), (w-100,h-70)]], dtype=np.int32)
    mask = np.zeros_like(edges) # mask = img와 같은 크기의 빈 이미지    

    if len(edges.shape) > 2: color = (255,255,255)  # Color        
    else: color = 255  # 흑백 

    cv2.fillPoly(mask, vertices, color)  #다각형부분(ROI 설정부분) color로 채움 
    ROI_image = cv2.bitwise_and(edges, mask) # 이미지와 color로 채워진 ROI를 합침
    
    # 3.허프변환 직선 검출
    lines = cv.HoughLinesP(ROI_image, 1, np.pi / 180., 160,  
                                minLineLength=100, maxLineGap=5)
    dst = np.zeros((ROI_image.shape[0], ROI_image.shape[1], 3), dtype=np.uint8)   

    if lines is not None:
        for i in range(0, len(lines)):
            l = lines[i][0]
            cv.line(dst, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv.LINE_AA)

    result = cv2.addWeighted(dst, 1, src, 1, 0.)
    cv.imshow("Source", src)
    cv.imshow("ROI_image", ROI_image)        
    cv.imshow("result", result)

    key = cv2.waitKey(10)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()