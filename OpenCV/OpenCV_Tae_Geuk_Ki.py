import cv2
import sys

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    cv2.imshow('gray', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    # cv2.imshow('inversed', ~frame)
    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows()    