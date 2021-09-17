import cv2
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if success:
        for code in pyzbar.decode(frame):
            print("인식 성공: ",code.data.decode('utf-8'))
        
        cv2.imshow('cam',frame)

        key = cv2.waitKey(1)
        if key == 27:
            break
cap.release()
cv2.destroyAllWindows()        
