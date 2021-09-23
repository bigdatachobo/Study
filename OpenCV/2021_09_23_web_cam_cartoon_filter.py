import numpy as np
import cv2

def cartoon_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w//2, h//2))
    blr = cv2.bilateralFilter(img2, -1, 20, 7)
    edge = 255 - cv2.Canny(img2, 80, 120)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    dst = cv2.bitwise_and(blr, edge)
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)
    return dst

def pencil_sketch_filter(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (0, 0), 3)
    dst = cv2.divide(gray, blr, scale=255)
    return dst

cap = cv2.VideoCapture(0)
toggle = 0
while True:
    key = cv2.waitKey(1)
    ret, frame = cap.read()
    # 좌우 반전
    frame = cv2.flip(frame,1)
    if not ret:
        break

    if toggle % 3 == 1:
        cf = cartoon_filter(frame)
        cv2.imshow('cam',cf)

    elif toggle % 3 == 2:
        psf = pencil_sketch_filter(frame)        
        cv2.imshow('cam',psf)
    else:
        cv2.imshow('cam', frame)

    if key == ord(' '):
        toggle += 1

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()