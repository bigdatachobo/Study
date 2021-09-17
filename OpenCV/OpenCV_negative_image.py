import cv2
import sys
import os
import re
os.chdir('C:/Users/PC021/Downloads/05-컴퓨터비전-이미지파일/05-컴퓨터비전-이미지파일')
file = 'images/cat.jpg'
img = cv2.imread(file)
title = re.findall(r'^\w+/(\w+).', file)[0]

cv2.imshow(title, img)

ESC_key = 27
while True:
    key = cv2.waitKey()
    if key == ESC_key:
        break
    elif key == ord('s') or key == ord('S'):
        img = ~img
        cv2.imshow("not image "+title, img)
        # img = ~img
cv2.destroyAllWindows()