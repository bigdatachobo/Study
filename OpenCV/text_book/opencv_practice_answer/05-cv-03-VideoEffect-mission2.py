# [2개 동영상 재생] - 순차 재생 중간에 동영상 전환 효과 넣기
import sys
import cv2
import numpy as np

# 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture('videos/video1.mp4')
cap2 = cv2.VideoCapture('videos/video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정함
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS) # 초당 프레임 수
effect_frames = int(fps * 2)

print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print('FPS:', fps)

delay = int(1000/fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 1번 동영상의 일부분 재생
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    out.write(frame1)   # 프레임 저장하기

    cv2.imshow('frame', frame1)
    cv2.waitKey(1)

# 2개의 동영상 합성한 후 재생
for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()  

    #A.밀어내기 방식으로 합성
    dx = int(w * i / effect_frames)   # 합성
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    frame[:, dx:w, :] = frame1[:, dx:w, :]

    # B.디졸브 방식으로 합성 (가중치를 변화시켜 효과부여)
    # alpha = 1.0 - (i / effect_frames)
    # frame = cv2.addWeighted(frame1, alpha, frame2, 1 - alpha, 0)
    # # alpha = i / effect_frames
    # frame = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)

    out.write(frame)   # 프레임 저장하기

    cv2.imshow('frame', frame)
    cv2.waitKey(1)

# 2번 동영상 재생하면서 저장
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        break

    out.write(frame2)   # 프레임 저장하기    

    cv2.imshow('frame', frame2)
    cv2.waitKey(1)

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
