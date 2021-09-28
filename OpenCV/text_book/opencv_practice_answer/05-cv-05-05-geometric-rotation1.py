import sys
import numpy as np
import cv2
import math

src = cv2.imread('images/parasol.jpg')  

if src is None:
    print('Image load failed!')
    sys.exit()

rad = 20 * math.pi / 180
print(f'pi: {math.pi} rad: {rad}')
print(f'cos: {math.cos(rad)} sin: {math.sin(rad)}')
aff = np.array([[math.cos(rad), math.sin(rad), 0],
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
