import cv2
import numpy as np

img = np.full((400,600,3), (255,255,255), dtype=np.uint8)

blue = (255,0,0)
red = (0,0,255)

# 타원 그리기
cv2.ellipse(img, (300,200), (100,100), -8, 0, 180, blue, -1)
cv2.ellipse(img, (300,200), (100,100), -8, 180, 360, red, -1)
cv2.ellipse(img, (349,194), (50,50), -8, 180, 360, blue, -1)
cv2.ellipse(img, (250,208), (49,49), -8, 0, 180, red, -1)

# 텍스트 삽입
cv2.putText(img, 'Tae Geuk Ki', (100,50), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,0), 3)

cv2.imshow('circle',img)
cv2.waitKey()
cv2.destroyAllWindows()