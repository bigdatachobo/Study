import cv2
import os
os.chdir('C:/Users/PC021/Downloads/05-컴퓨터비전-이미지파일/05-컴퓨터비전-이미지파일')

def logo_maker(addr):
    src = cv2.imread('images/cat.bmp', cv2.IMREAD_COLOR)
    logo = cv2.imread(addr, cv2.IMREAD_UNCHANGED)

    # mask - alpha 채널 한개만 사용
    mask = logo[:,:,3]

    logo = logo[:,:,:-1]
    h,w = mask.shape[:2]
    crop = src[10:10+h, 10:10+w]
    img = cv2.copyTo(logo, mask, crop)
    # 원본 그림 사본 지정
    img2 = src.copy()
    for i in range(10,10+h):
        for j in range(10,10+w):
            img2[i][j] = img[i-10][j-10]
    cv2.imshow('image',img2)
    cv2.waitKey()


for i in ['images/intel.png', 'images/apple.png']:
    logo_maker(i)
cv2.destroyAllWindows()    