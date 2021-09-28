import numpy as np
import cv2

def getGrayHistImage(hist):
    #h, w = (200, 256*2)
    h, w = (100, 256)
    imgHist = np.full((h, w), 255, dtype=np.uint8)

    histMax = np.max(hist)
    print(f'histMax:{histMax}')
    for x in range(256):
        print(f'x:{x} - y: {int(hist[x, 0] * 100 / histMax)}')
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        # pt1 = (x*2, 150)
        # pt2 = (x*2, 150 - int(hist[x, 0] * 150 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)

cv2.imshow('src', src)
cv2.imshow('histImg', histImg)
cv2.waitKey()
cv2.destroyAllWindows()