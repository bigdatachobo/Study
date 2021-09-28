# datetime.timedelta 참고: https://wikidocs.net/104836

import datetime
import numpy as np
import cv2

cap = cv2.VideoCapture('videos/video1.mp4') # 비디오 열기

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 비디오 프레임 크기 출력
fps = round(cap.get(cv2.CAP_PROP_FPS))
delay = round(1000 / fps)
print(f'fps:{fps} delay:{delay}')

tm = cv2.TickMeter()
tm.reset()
tm.start()
while True:     # 카메라 프레임 처리
    ret, frame = cap.read()

    if not ret: break

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 27:
        break

tm.stop()
print('Elapsed time: {} ms.'.format(tm.getTimeMilli()))
print('Elapsed time: {} s.'.format(str(datetime.timedelta(milliseconds=tm.getTimeMilli()))))


cap.release()
cv2.destroyAllWindows()