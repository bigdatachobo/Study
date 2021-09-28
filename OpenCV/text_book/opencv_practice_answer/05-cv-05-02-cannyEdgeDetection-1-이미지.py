# 엣지 검출
import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/car.jpg', cv2.IMREAD_GRAYSCALE)

canny1 = cv2.Canny(img, 50, 200)
canny2 = cv2.Canny(img, 100, 200)
canny3 = cv2.Canny(img, 170, 200)

titles = ['original','canny1','canny2','canny3' ]
images = [img, canny1, canny2, canny3]

cv2.imshow(titles[0], img)
cv2.imshow(titles[1], canny1)
cv2.imshow(titles[2], canny2)
cv2.imshow(titles[3], canny3)
cv2.waitKey()
cv2.destroyAllWindows()

plt.figure(figsize=(10,10))
for i in range(len(titles)):
    plt.subplot(2,2,i+1)
    plt.title(titles[i])
    plt.show(images[i], cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()