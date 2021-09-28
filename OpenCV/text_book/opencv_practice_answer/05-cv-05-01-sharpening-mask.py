import sys
import numpy as np
import cv2

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# mask = np.array([[0, -1, 0],
#                    [-1, 5, -1],
#                    [0, -1, 0]])
mask = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])                   
dst = cv2.filter2D(src, -1, mask)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()