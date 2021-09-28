import matplotlib.pyplot as plt
import cv2

# 컬러 영상 & 그레이스케일 영상 불러오기
img1 = 'images\cat.bmp'
img2 = 'images\penguin.jpg'
img1BGR = cv2.imread(img1)
img2BGR = cv2.imread(img2)
img1RGB = cv2.cvtColor(img1BGR, cv2.COLOR_BGR2RGB)
img2RGB = cv2.cvtColor(img2BGR, cv2.COLOR_BGR2RGB)
img1Gray = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
img2Gray = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)

# 두 개의 영상을 함께 출력
plt.subplot(221), plt.axis('off'), plt.imshow(img1RGB)
plt.subplot(222), plt.axis('off'), plt.imshow(img1Gray, cmap='gray')
plt.subplot(223), plt.axis('off'), plt.imshow(img2RGB)
plt.subplot(224), plt.axis('off'), plt.imshow(img2Gray, cmap='gray')
plt.show()
