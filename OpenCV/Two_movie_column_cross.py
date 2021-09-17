import cv2
import os
import numpy as np

os.chdir('C:/Users/PC021/Downloads/05-컴퓨터비전-이미지파일/05-컴퓨터비전-이미지파일')
cap1 = cv2.VideoCapture('videos/video1.mp4')
cap2 = cv2.VideoCapture('videos/video2.mp4')

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D','I','V','X'
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

for _ in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()
    cv2.imshow('frame', frame1)
    cv2.waitKey(5)

for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    dx = int( w * i / effect_frames)

    frame = np.zeros((h,w,3), dtype=np.uint8)
    
    frame[:, 0: w - dx, :] = frame1[:, 0: w - dx, :] # 우측에서부터 사라짐
    frame[:, w - dx:w, :] = frame2[:, w - dx:w, :]
    
    # frame[:, 0: dx, :] = frame1[:, 0: dx, :] # 좌측에서부터 사라짐
    # frame[:, dx:w, :] = frame2[:, dx:w, :]

    out.write(frame1)
    cv2.imshow('frame', frame)
    cv2.waitKey(5)

for _ in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        break

    elif cv2.waitKey(5) == 27:
        break

    out.write(frame2)
    cv2.imshow('frame',frame2)

cap1.release()
cap2.release()

out.release()
cv2.destroyAllWindows()
