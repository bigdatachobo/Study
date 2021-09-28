import cv2
import matplotlib.pyplot as plt

# 컬러 영상 출력
imgBGR = cv2.imread('images/cat.jpg')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
# b, g, r = cv2.split(imgBGR)   # img파일을 b,g,r로 분리
# imgRGB = cv2.merge([r,g,b]) # b, r을 바꿔서 Merge

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('images/cat.jpg', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
