import sys
import cv2

cap = cv2.VideoCapture(0) 

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D','I','V','X'
out = cv2.VideoWriter('output.avi', fourcc, 30, (w, h))

while True:     # 카메라 프레임 처리
    ret, frame = cap.read()

    inversed = ~frame  # 반전
    out.write(inversed)

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
