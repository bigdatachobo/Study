# [2개 동영상 재생] - 순차 재생
import sys
import cv2

# 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture('videos/video1.mp4')
cap2 = cv2.VideoCapture('videos/video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정함
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)

print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print('FPS:', fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 1번 동영상 재생하면서 저장
while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    out.write(frame1)   # 프레임 저장하기

    cv2.imshow('frame', frame1)
    cv2.waitKey(1)

# 2번 동영상 재생하면서 저장
while True:
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
