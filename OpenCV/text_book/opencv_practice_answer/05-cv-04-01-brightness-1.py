import numpy as np
import cv2
import matplotlib.pyplot as plt


# 그레이스케일 영상 불러오기
src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

#dst1 = cv2.add(src, 100)
dst1 = np.clip(src + 100., 0, 255).astype(np.uint8)
dst2 = cv2.add(src, 255)
dst3 = cv2.add(src, -100)
dst4 = cv2.add(src, -255)


cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.waitKey()
cv2.destroyAllWindows()

# plt.subplot(221), plt.axis('off'), plt.imshow(dst1, cmap='gray')
# plt.subplot(222), plt.axis('off'), plt.imshow(dst2, cmap='gray')
# plt.subplot(223), plt.axis('off'), plt.imshow(dst3, cmap='gray')
# plt.subplot(224), plt.axis('off'), plt.imshow(dst4, cmap='gray')
# plt.show()


