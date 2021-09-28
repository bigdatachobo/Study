# YOLOv3 Object(객체) 검출하기 - 동영상
import sys
import cv2
import numpy as np
import time
import io
import base64
from IPython.display import HTML

model = 'yolo_v3/yolov3.weights'
config = 'yolo_v3/yolov3.cfg'
class_labels = 'yolo_v3/coco.names'

files = ['seoul', 'india', 'street']    # Detection 할 원본 동영상
file_name = 'videos/'+files[2]+'.mp4'   # Detection 할 원본 동영상
output_name = 'videos/'+files[2]+'_out.mp4'   # Detection 된 output 동영상 
min_confidence = 0.5            # detection 으로 인정할 최소 확률(신뢰도) 지정
elapsed_time = 0                # 총 경과시간 초기화 


# YOLO Object검출 및 출력
def detectAndDisplay(frame):
    start_time = time.time()

    img = cv2.resize(frame, None, fx=0.9, fy=0.9)
    height, width, channels = img.shape

    # YOLOv3의 Detecting model 3가지(320×320, 416×416, 608×608)
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []      # detection 한 Class id를 저장하는 배열 정의
    confidences = []    # detection 한 Class 의 신뢰도(확률)를 저장하는 배열 정의
    boxes = []          # detection 한 boxing 정보를 저장하는 배열 정의

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)      # detection 한 Class id
            confidence = scores[class_id]     # detection 한 Class 의 신뢰도(확률)

            if confidence > min_confidence:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])             # boxing 정보를 boxes 배열에 저장
                confidences.append(float(confidence))  # 신뢰도(확률)을 confidences 배열에 저장
                class_ids.append(class_id)             # Class id 를 class_ids 배열에 저장
    
    # apply non-max suppression
    # 박스안에 박스(노이즈)를 하나로 만들어 준다.
    # (40%이상 겹치는 바운딩 박스에 대해 최대 confidence>0.5인 바운딩 박스만 선별)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, min_confidence, 0.4)    
    font = cv2.FONT_HERSHEY_PLAIN

    for i in range(len(boxes)):
        if i in indexes:    # 노이즈가 제거된 박스만 표시해 준다.   
            x, y, w, h = boxes[i]
            label = "{}: {:.2f}".format(classes[class_ids[i]], confidences[i]*100)    # Class 이름, 신뢰도(확률) 표시 
            print('--', i, label)

            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
            cv2.rectangle(img, (x, y - 20), (x + w, y), color, -1)
            cv2.putText(img, label, (x + 5, y - 5), font, 1, (255, 255, 255), 1)
    
    process_time = time.time() - start_time
    global elapsed_time
    elapsed_time += process_time   # 총 경과시간 누적
    print("=== A frame took {:.3f} seconds".format(process_time))

    # img(frame을 resize한)을 파일에 저장한다.
    global writer

    if writer is None and output_name is not None:
        # fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        # writer = cv2.VideoWriter(output_name, fourcc, 30,
        #         (img.shape[1], img.shape[0]), True)
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        writer = cv2.VideoWriter(output_name, fourcc, 30, (img.shape[1], img.shape[0]))
        #writer = cv2.VideoWriter(output_name, fourcc, fps, (w, h))

    if writer is not None:
        writer.write(img)



# YOLO 로드 (가중치 파일, CFG 파일)
net = cv2.dnn.readNet(model, config)  
if net.empty():
    print('Net open failed!')
    sys.exit()


# YOLO 클래스 이름 불러오기
# class_labels 파일에 정의된 80개의 Object의 이름을 classes 배열에 넣어준다.
classes = []  # detection 할 Object(Class) list 배열을 정의
with open(class_labels, "r") as f:
    classes = [line.strip() for line in f.readlines()] 


# 출력 레이어 이름 받아오기    
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


# Object 마다 컬러를 하나씩 다르게 지정
colors = np.random.uniform(0, 255, size=(len(classes), 3))  # Object 마다 컬러를 하나씩 다르게 지정


# 원본 동영상에서 video stream을 읽어온다.
cap = cv2.VideoCapture(file_name)
if not cap.isOpened:
    print('--video open failed!')
    sys.exit()

# 동영상 frame개수, fps
frame_cnt = round(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
print('--frame_cnt:', frame_cnt, ' FPS:', fps)

writer = None
while True:
    # 웹캠 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        break

    if frame is None:
        print('--(!) No captured frame -- Break!')
        print("elapsed time {:.3f} seconds".format(elapsed_time))
        break

    cv2.imshow('frame', frame)
    cv2.waitKey(1)        

    detectAndDisplay(frame)

cap.release()       # close the video file pointers
out.release()    # close the out point
cv2.destroyAllWindows()


