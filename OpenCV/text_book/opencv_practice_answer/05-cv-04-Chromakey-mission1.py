# 크로마키 영상 만들기-스페이스키 누르면 배경넣기
import sys
import numpy as np
import cv2

src_file = 'videos/woman.mp4'       #녹색 배경 영상
mask_file = 'videos/raining.mp4'    #녹색 배경에 들어갈 영상

# 녹색 동영상
cap1 = cv2.VideoCapture(src_file)
if not cap1.isOpened():
    print('video open failed!')
    sys.exit()

# 비오는 배경 동영상
cap2 = cv2.VideoCapture(mask_file)
if not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)
print(f'frame_cnt1: {frame_cnt1}')
print(f'frame_cnt2: {frame_cnt2}')
print(f'fps: {fps}, delay: {delay}')

#출력할 동영상 정보 지정
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D','I','V','X'
out = cv2.VideoWriter('videos/chromakey_out.avi', fourcc, 30, (w, h))
print(f'w: {w}, h: {h}')

# 전체 동영상 재생
while True:
    ret1, frame1 = cap1.read()
    if not ret1: break
    frame = frame1.copy()
    
    ret2, frame2 = cap2.read()
    if not ret2: break

    # HSV 색 공간에서 녹색 영역을 검출하여 합성
    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)   #HSV:색상Hue 채도Saturation 명도Value
    mask = cv2.inRange(hsv, (50, 150, 0), (80, 255, 255))
    cv2.copyTo(frame2, mask, frame)    #cv2.copyTo(src, mask, dst=None) 

    # 파일에 출력하기
    out.write(frame)

    # 화면에 동영상 출력하기
    cv2.imshow('frame1', frame1)
    cv2.imshow('frame2', frame2)
    cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(delay)
    if key == 27: #esc
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
