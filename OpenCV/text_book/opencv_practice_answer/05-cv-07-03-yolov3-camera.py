# YOLOv3 Object(객체) 검출하기 - 실시간 카메라 
import sys
import cv2
import numpy as np

model = 'yolo_v3/yolov3.weights'
config = 'yolo_v3/yolov3.cfg'
class_labels = 'yolo_v3/coco.names'


# YOLO 로드 (가중치 파일, CFG 파일)
net = cv2.dnn.readNet(model, config)
if net.empty():
    print('Net open failed!')
    sys.exit()


# YOLO 클래스 이름 불러오기
classes = []
with open(class_labels, "r") as f:
    classes = [line.strip() for line in f.readlines()]


# 출력 레이어 이름 받아오기    
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


# 웹캠 신호 받기
cap = cv2.VideoCapture(0)
if not cap.isOpened:
    print('--video open failed!')
    sys.exit()

while True:
    # 웹캠 프레임 읽기
    ret, frame = cap.read()
    h, w, c = frame.shape   # h:height, w:width, c:channels
   
    # YOLO 입력: YOLOv3의 Detecting model 3가지(320×320, 416×416, 608×608)
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)    

    # Showing informations on the screen
    class_ids = []      # detection 한 Class id를 저장하는 배열 정의
    confidences = []    # detection 한 Class 의 신뢰도(확률)를 저장하는 배열 정의
    boxes = []          # detection 한 boxing 정보를 저장하는 배열 정의

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                # Object detected
                # 바운딩 박스 중심 좌표 & 박스 크기
                cx = int(detection[0] * w)  #cx:center_x
                cy = int(detection[1] * h)  #cy:center_y
                dw = int(detection[2] * w)
                dh = int(detection[3] * h)

                # Rectangle coordinate
                # 바운딩 박스 좌상단 좌표
                x = int(cx - dw / 2)
                y = int(cy - dh / 2)

                boxes.append([x, y, dw, dh])            # boxing 정보를 boxes 배열에 저장
                confidences.append(float(confidence))   # 신뢰도(확률)을 confidences 배열에 저장
                class_ids.append(class_id)              # Class id 를 class_ids 배열에 저장

    # apply non-max suppression
    # 박스안에 박스(노이즈)를 하나로 만들어 준다.
    # (40%이상 겹치는 바운딩 박스에 대해 최대 confidence>0.5인 바운딩 박스만 선별)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.45, 0.4)


    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            score = confidences[i]

            # 경계상자와 클래스 정보 이미지에 입력
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
            cv2.putText(frame, label, (x, y - 20), cv2.FONT_ITALIC, 0.5, 
            (255, 255, 255), 1)

    cv2.imshow("YOLOv3", frame)

    if cv2.waitKey(100) > 0:
        break