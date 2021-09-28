import cv2
import sys

# 카메라 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

file = 'photo.jpg'
top, bottom, right, left = 50, 50, 50, 50
while True:
    ret, frame = cap.read()

    if not ret: break


    font = cv2.FONT_HERSHEY_DUPLEX
    text1 = "*Press 'Enter' key!!!"
    text2 = "FileLoc: C:\\python\rapa\photo.jpg"
    cv2.putText(frame, text1, (left, top), font, 1, (0, 0, 255), 1)
    cv2.putText(frame, text2, (50, 450), font, 0.5, (255, 255, 255), 1)
    cv2.rectangle(frame, (180, 90), (500, 400), (255, 255, 255), 3)  
    
    cv2.flip(frame,1)   #이미지 반전  1:좌우, 0:상하
    cv2.imshow("Frame", frame)
    # resize_frame = cv2.resize(frame, (800, 600))            
    # cv2.imshow("Frame", resize_frame)
    # cv2.moveWindow("Frame", 300, 50) 

    key = cv2.waitKey(10)
    if key == 27: break
    elif key == 13  :  #키보드 엔트키: 화면 저장
        img_frame = frame.copy()
        img_size = img_frame[90:400, 180:500]    # 위 흰색 영역만큼 사이즈 잘라 저장하기 img_frame[start_y:end_y, s_x:e_x]
        cv2.imwrite(file, img_size)
        print(file, ' 저장됨')
    
cap.release()
cv2.destroyAllWindows()
