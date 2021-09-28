import sys
import glob
import cv2


# 1.특정 폴더의 이미지 파일을 모두 img_files 리스트에 추가
#img_files = glob.glob('.\\images\\*.jpg')
img_files = glob.glob('images/*.jpg')

if not img_files:
    print("There are no jpg files in 'images' folder")
    sys.exit()

print(img_files)

# 2.전체 화면으로 'image' 창 생성
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx = 0
while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print('Image load failed!')
        break

    cv2.imshow('image', img)
    if cv2.waitKey(1000) >= 0:
        break

    idx += 1
    
cv2.destroyAllWindows()
