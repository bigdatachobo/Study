import cv2  
import numpy as np

image = np.zeros((300,400), np.uint8)
image.fill(200)               # image[:] = 200

cv2.imshow('Window Title', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
