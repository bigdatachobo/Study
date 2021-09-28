import time
import numpy as np
import cv2

img = cv2.imread('images/road_evening.jpg')

tm = cv2.TickMeter()

tm.reset()
tm.start()
t1 = time.time()

edge = cv2.Canny(img, 50, 150)

tm.stop()
print('time:', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))

