import numpy as np
import cv2
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src_file = 'videos/woman.mp4'
mask_file = 'videos/raining.mp4'

cap1 = cv2.VideoCapture(src_file) # 녹색 동영상
cap2 = cv2.VideoCapture(mask_file) # 비오는 배경 동영상

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print(f'fps: {fps}, delay: {delay}')

do_composit = False
while True:
    key = cv2.waitKey(delay-30)
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # HSV 색 공간에서 녹색 영역을 검출하여 합성
    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV) #HSV:색상Hue 채도Saturation 명도Value

    if do_composit:
        mask = cv2.inRange(hsv, (50, 150, 0), (80, 255, 255))
        gb_mask = cv2.GaussianBlur(mask,(0,0),3)
        dst = np.clip(2.0*mask - gb_mask, 0, 255).astype(np.uint8)
        cv2.copyTo(frame2, dst, frame1) #cv2.copyTo(src, mask, dst=None)
        cv2.imshow('mask', mask)
        cv2.imshow('bf_mask',gb_mask)
        cv2.imshow('dst',dst)


    cv2.imshow('frame', frame1)

    if key == ord(' '):
        do_composit = not do_composit

    if cv2.waitKey(delay-30) == 27:                    
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()