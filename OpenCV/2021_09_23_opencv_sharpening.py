import numpy as np
import cv2
import os
os.chdir('C:/Users/PC021/Documents/vscode_python/OPENCV_course')

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

# 원본 
src_f = src.astype(np.float32)

# unsharp mask
blr = cv2.GaussianBlur(src_f, (0, 0), 2)

# 2 * 원본 - blurring
sharpeing = np.clip(2.0*src_f - blr, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', sharpeing)
cv2.waitKey()
cv2.destroyAllWindows()