import sys
import os
import cv2
import re
import numpy as np

os.chdir('C:/Users/PC021/Downloads/05-컴퓨터비전-이미지파일/05-컴퓨터비전-이미지파일')
file = 'images/car_sports_car_neon_157154_1024x768.jpg'
image = cv2.imread(file,cv2.IMREAD_GRAYSCALE)
image_gray = cv2.imwrite('images/car_sports_car_neon_gray.jpg',image,[cv2.IMWRITE_JPEG_QUALITY, 90 ])
if image is None:
    print('Image load failed!')
    sys.exit()
cv2.imshow(re.findall(r'^images/(\w+).',file)[0], image)
cv2.waitKey(0)
cv2.destroyAllWindows()