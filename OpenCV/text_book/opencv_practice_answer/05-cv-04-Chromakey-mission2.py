import sys
import cv2
import numpy as np


# 녹색 배경 동영상
cap1 = cv2.VideoCapture('videos/woman.mp4')
if not cap1.isOpened():
    print('video open failed!')
    sys.exit()

# 비오는 배경/구름 배경 동영상
#cap2 = cv2.VideoCapture('videos/raining.mp4')
cap2 = cv2.VideoCapture('videos/cloud.mp4')
if not cap2.isOpened():
    print('video open failed!')
    sys.exit()
 
# 세 동영상의 크기, FPS는 같다고 가정
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)
print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print(f'fps: {fps}, delay: {delay}')

# 합성 여부 플래그
do_composit = False

# 전체 동영상 재생
while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break
    
    # do_composit 플래그가 True일 때에만 합성
    if do_composit:
        ret2, frame2 = cap2.read()

        if not ret2:
            break

        # HSV 색 공간에서 녹색 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))
        cv2.copyTo(frame2, mask, frame1)

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    # 스페이스바를 누르면 do_composit 플래그를 변경
    if key == ord(' '):
        do_composit = not do_composit
    elif key == 27:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
