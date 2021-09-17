import os
import re
import numpy as np
import cv2

os.chdir('C:/Users/PC021/Downloads/05-컴퓨터비전-이미지파일/05-컴퓨터비전-이미지파일')
file = 'images/cat.bmp'
winname = re.findall(r'^\w+/(\w+).',file)[0]
image = cv2.imread(file, cv2.IMREAD_COLOR)
H,W,_ = image.shape

cv2.imshow(winname, image)
cv2.resizeWindow(winname, W, H)

cv2.imshow(winname + '+100', image)
cv2.resizeWindow(winname + '+100', W + 100, H + 100)

cv2.moveWindow(winname,300,300)

cv2.waitKey()
cv2.destroyAllWindows()