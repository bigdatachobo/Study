# 엣지 검출 - 동영상
import cv2 
import numpy as np
import matplotlib.pyplot as plt

def onChange(pos):
    pass

def edge_tracking():
    try:
        print('비디오 재생')
        #video = 'videos/solidWhiteRight.mp4'
        video = 'videos/road5.mp4'
        cap = cv2.VideoCapture(video)
        
        title = 'edge traking'
        cv2.namedWindow(title)
        cv2.createTrackbar('low threshold', title, 0, 255, onChange)
        cv2.createTrackbar('high threshold', title, 0, 255, onChange)
    except:
        print('비디오 재생 실패')
        return

    while True:
        ret, frame = cap.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

            if cv2.waitKey(33) == 27:
                break

            low = cv2.getTrackbarPos('low threshold', title)
            high = cv2.getTrackbarPos('high threshold', title)
        
            if (low==0) and (high==0):
                cv2.imshow(title, frame)
            elif low > high:
                print('Low threshold must be low than high threshold!')
                continue
            else:
                frame = cv2.Canny(frame, low, high)
                cv2.imshow(title, frame)
        else:
            print('비디오 종료')
            break

    cap.release()
    cv2.destroyAllWindows()

edge_tracking()