import cv2
import os
from copy import deepcopy
os.chdir('C:/Users/PC021/Downloads/05-컴퓨터비전-이미지파일/05-컴퓨터비전-이미지파일')

def color(pos,i):
    img[:,:,i] = pos % 256
    cv2.imshow('image', img)
    
img = cv2.imread('images/object.jpg')

cv2.namedWindow('image')
# BGR
for col_idx, col_name in enumerate(['Blue','Green','Red']):
     cv2.createTrackbar( col_name, 'image', 0, 255, lambda pos: color(pos,col_idx))

cv2.waitKey()
cv2.destroyAllWindows()