import sys
import os
import cv2
import re
import numpy as np

os.chdir('C:/Users/PC021/Downloads/05-컴퓨터비전-이미지파일/05-컴퓨터비전-이미지파일')
file1 = 'images/airplane.bmp'
file2 = 'images/rapa_logo.PNG'
image1 = cv2.imread(file1, cv2.IMREAD_UNCHANGED)
image2 = cv2.imread(file2, cv2.IMREAD_UNCHANGED)
print(image1.shape)
print(image2.shape)
if image1 is None:
    print('Image load failed!')
    sys.exit()
cv2.imshow(re.findall(r'^images/(\w+).',file1)[0], image1)
cv2.imshow(re.findall(r'^images/(\w+).',file2)[0], image2)
cv2.waitKey(0)
cv2.destroyAllWindows()