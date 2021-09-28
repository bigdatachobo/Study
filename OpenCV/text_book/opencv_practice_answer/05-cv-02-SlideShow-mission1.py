import sys
import cv2


# 1.특정 폴더의 이미지 파일을 모두 img_files 리스트에 추가
# os 모듈 이용
import os
file_list = os.listdir('images')
img_files = [file for file in file_list if file.endswith('.jpg')]

# glob 모듈 이용
import glob
img_files = glob.glob('images/*.jpg')
#img_files = glob.glob('.\\images\\*.jpg')

if not img_files:
    print("There are no jpg files in 'images' folder")
    sys.exit()

print(img_files)
