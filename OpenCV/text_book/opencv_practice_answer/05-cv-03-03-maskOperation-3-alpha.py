import cv2
import numpy as np

img = np.zeros((480, 480, 3), np.uint8)
#img = np.full((480, 480,3), 255, np.uint8)

cv2.line(img, (10,10), (100,100),(0,255,255), 5)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
