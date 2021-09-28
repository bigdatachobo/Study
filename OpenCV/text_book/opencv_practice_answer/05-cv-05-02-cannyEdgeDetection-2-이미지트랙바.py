# 엣지 검출 - 트랙바 사용
import cv2 
import numpy as np
import matplotlib.pyplot as plt

def onChange(pos):
    pass

def edge_detection():
    img = cv2.imread('images/car.jpg', cv2.IMREAD_GRAYSCALE)
    title = 'edge detection'
    cv2.namedWindow(title)

    cv2.createTrackbar('low threshold', title, 0, 255, onChange)
    cv2.createTrackbar('high threshold', title, 0, 255, onChange)
    cv2.imshow(title, img)

    while True:
        if cv2.waitKey(33) == 27:
            break

        low = cv2.getTrackbarPos('low threshold', title)
        high = cv2.getTrackbarPos('high threshold', title)
        
        if (low==0) and (high==0):
            cv2.imshow(title, img)
        elif low > high:
            print('Low threshold must be low than high threshold!')
        else:
            canny = cv2.Canny(img, low, high)
            cv2.imshow(title, canny)

    cv2.destroyAllWindows()

edge_detection()