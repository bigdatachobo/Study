import cv2
import numpy as np
import random
import os
os.chdir('C:/Users/PC021/Downloads/05-컴퓨터비전-이미지파일/05-컴퓨터비전-이미지파일')
oldx = oldy = -1

def random_color():
    return tuple(sorted([i for i in range(256)]*3, key=lambda x:random.random())[:3])

def random_size():
    return random.randint(10,100)

def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y

    elif event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (oldx, oldy),random_size(),random_color(),-1,cv2.LINE_4,)
        cv2.imshow('image', img)
        oldx, oldy = x, y

img = cv2.imread('images/car.jpg',cv2.IMREAD_UNCHANGED)

cv2.imshow('image', img)
cv2.setMouseCallback('image', on_mouse, img)
cv2.waitKey()
cv2.destroyAllWindows()
