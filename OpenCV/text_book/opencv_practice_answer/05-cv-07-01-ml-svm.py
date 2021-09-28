import sys
import numpy as np
import cv2


trains = np.array([[150, 200], [200, 250],
                   [100, 250], [150, 300],
                   [350, 100], [400, 200],
                   [400, 300], [350, 400]], dtype=np.float32)
labels = np.array([0, 0, 0, 0, 1, 1, 1, 1])

svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)    # 선형커널
#svm.setKernel(cv2.ml.SVM_RBF)      # 방사 기저함수 커널
#svm.setKernel(cv2.ml.SVM_SIGMOID)  # 시그모이드 커널
#svm.setKernel(cv2.ml.SVM_CHI2)     # 지수 카이 제곱 커널
#svm.setKernel(cv2.ml.SVM_INTER)    # 히스토그램교차 커널

svm.trainAuto(trains, cv2.ml.ROW_SAMPLE, labels)
print('C:', svm.getC())
print('Gamma:', svm.getGamma())

w, h = 500, 500
img = np.zeros((h, w, 3), dtype=np.uint8)

for y in range(h):
    for x in range(w):
        test = np.array([[x, y]], dtype=np.float32)
        _, res = svm.predict(test)
        ret = int(res[0, 0])

        if ret == 0:
            img[y, x] = (128, 128, 255)  # Red
        else:
            img[y, x] = (128, 255, 128)  # Green

color = [(0, 0, 128), (0, 128, 0)]

for i in range(trains.shape[0]):
    x = int(trains[i, 0])
    y = int(trains[i, 1])
    l = labels[i]

    cv2.circle(img, (x, y), 5, color[l], -1, cv2.LINE_AA)

cv2.imshow('svm', img)
cv2.waitKey()
cv2.destroyAllWindows()
