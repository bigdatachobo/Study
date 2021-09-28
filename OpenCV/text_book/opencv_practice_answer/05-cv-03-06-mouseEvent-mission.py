import numpy as np
import cv2


oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDBLCLK:
        radius = np.random.randint(10,100)
        R = np.random.randint(0,255)
        G = np.random.randint(0,255)
        B = np.random.randint(0,255)
        #cv2.circle(img,(x,y), radius,(R,G,B),-1)
        pts = np.array([[x+10,y+10],[x,y-50],[x+50,y],[x-40,y-20],[x+60,y-30]])
        #cv2.polylines(img,[pts],True,(rd.randint(10,255),rd.randint(10,255),rd.randint(10,255)),5)
        cv2.polylines(img,[pts],True,(R,G,B),5)
        
        cv2.imshow('image', img)


#img = np.ones((480, 640, 3), dtype=np.uint8) * 255
img = np.full((480, 640,3),(255,255,255),dtype=np.uint8)


cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
