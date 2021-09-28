import sys
import numpy as np
import cv2

oldx = oldy = -1

file = 'images/handwrite_digit.jpg'
# 숫자 영상을 20x20 크기 안에 적당히 들어가도록 리사이즈
def norm_img(img):
    h, w = img.shape[:2]

    img = ~img
    blr = cv2.GaussianBlur(img, (0, 0), 2)

    sf = 14. / h  # scale factor. 위/아래 3픽셀씩 여백 고려.
    if w > h:
        sf = 14. / w

    img2 = cv2.resize(img, (0, 0), fx=sf, fy=sf, interpolation=cv2.INTER_AREA)
    h2, w2 = img2.shape[:2]
    a = (20 - w2) // 2
    b = (20 - h2) // 2
    

    dst = np.zeros((20, 20), dtype=np.uint8)
    dst[b:b+h2, a:a+w2] = img2[:, :]
    print('1--',h2, w2, a, b)
    print('2--',b,b+h2, a,a+w2)

    return dst

# 마우스 이벤트: 화면에 글자쓰기
def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 0), 5, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y

img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)
cv2.imshow('image', img)

while True:
    key = cv2.waitKey()
    if key == 13:  # ENTER 키
        cv2.imwrite(file, img)
        print(file, ' 저장됨')
        break
    elif key == 27:  # ESC 키
        cv2.destroyWindow('image')
        sys.exit()


# 입력 필기체 숫자 이미지 불러오기
src = cv2.imread(file)

if src is None:
    print('Image load failed!')
    sys.exit()

# HOG 객체 생성
hog = cv2.HOGDescriptor((20, 20), (10, 10), (5, 5), (5, 5), 9)

# 미리 학습된 SVM 데이터 불러오기
svm = cv2.ml.SVM_load('xml/svmdigits.yml')
print(svm)

# 이진화 & 레이블링
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
print(src_bin)
cnt, _, stats, _ = cv2.connectedComponentsWithStats(src_bin)

dst = src.copy()

for i in range(1, cnt):
    x, y, w, h, s = stats[i]
    print(x, y, w, h, s)

    if s < 100:
        continue

    # 각각의 숫자 부분 영상을 정규화한 후 HOG&SVM 숫자 인식
    digit = norm_img(src_gray[y:y+h, x:x+w])
    test_desc = hog.compute(digit).T
    _, res = svm.predict(test_desc)

    # HOG&SVM 숫자 인식 결과 출력
    cv2.rectangle(dst, (x, y, w, h), (0, 0, 255))
    cv2.putText(dst, str(int(res[0, 0])), (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
