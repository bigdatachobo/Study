import matplotlib.pyplot as plt
import cv2
import os
os.chdir('C:/Users/PC021/Downloads/05-컴퓨터비전-이미지파일/05-컴퓨터비전-이미지파일')
file = 'images/cat.bmp'
img_BGR = cv2.imread(file)\

# 자동
# img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

# 수동
b,g,r = cv2.split(img_BGR)
img_RGB = cv2.merge([r,g,b])

# 컬러 영상 출력
plt.axis('off')
plt.imshow(img_RGB)
plt.show()

# 그레이스케일 영상 출력
img_Gray = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(img_Gray, cmap='gray')
plt.show()