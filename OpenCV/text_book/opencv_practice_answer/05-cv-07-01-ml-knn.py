import numpy as np
import cv2

# 트랙바 이벤트
def on_k_changed(pos):
    global k_value

    k_value = pos
    if k_value < 1:
        k_value = 1

    trainAndDisplay()

# 데이터(좌표) 학습 및 좌표에 원 표시
def trainAndDisplay():
    trainData = np.array(train, dtype=np.float32)
    labelData = np.array(label, dtype=np.int32)

    knn.train(trainData, cv2.ml.ROW_SAMPLE, labelData)

    h, w = img.shape[:2]
    for y in range(h):
        for x in range(w):
            sample = np.array([[x, y]]).astype(np.float32)

            ret, _, _, _ = knn.findNearest(sample, k_value)

            ret = int(ret)
            if ret == 0:
                img[y, x] = (128, 128, 255)
            elif ret == 1:
                img[y, x] = (128, 255, 128)
            elif ret == 2:
                img[y, x] = (255, 128, 128)

    for i in range(len(train)):
        x, y = train[i]
        l = label[i][0]

        if l == 0:
            cv2.circle(img, (x, y), 5, (0, 0, 128), -1, cv2.LINE_AA)
        elif l == 1:
            cv2.circle(img, (x, y), 5, (0, 128, 0), -1, cv2.LINE_AA)
        elif l == 2:
            cv2.circle(img, (x, y), 5, (128, 0, 0), -1, cv2.LINE_AA)

    cv2.imshow('knn', img)


# 영상(화면) 크기
k_value = 1
img = np.full((500, 500, 3), 255, np.uint8)
knn = cv2.ml.KNearest_create()


# 학습용 랜덤 데이터 생성: 90개의 임의의 좌표 데이터 
# 학습 데이터 & 레이블
train = []
label = []

NUM = 30
rn  = np.zeros((NUM, 2), np.int32)
pos = [(150,150), (350, 150), (250, 400)]  
c_  = [0, 1, 2]   # 데이터 분류 레이블
rn = np.zeros((NUM, 2), np.int32)

# 총 90개의 임의의 좌표 데이터 생성
for idx, c in enumerate(c_):
    cv2.randn(rn, 0, 50)    #평균0, 표준편차50 정규분포를 따르는 난수 발생
    for i in range(NUM):
        train.append([rn[i, 0] + pos[idx][0], rn[i, 1] + pos[idx][1]])
        label.append([c])


# 영상 출력 창 생성 & 트랙바 생성
cv2.namedWindow('knn')
cv2.createTrackbar('k_value', 'knn', 1, 5, on_k_changed)

# KNN 결과 출력
trainAndDisplay()

cv2.waitKey()
cv2.destroyAllWindows()
