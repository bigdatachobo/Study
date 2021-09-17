import cv2
import os
import re
import glob
os.chdir('C:/Users/PC021/Downloads/05-컴퓨터비전-이미지파일/05-컴퓨터비전-이미지파일')
img_files = glob.glob('images/*')  

cnt = len(img_files)
idx = 0
ESC = 27

def title(inx):
    return re.findall(r'^\w+\\(\w+).', img_files[inx])[0]

def display(i):
    img = cv2.imread(img_files[i])
    cv2.namedWindow(title(i), cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(title(i), cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) 
    cv2.imshow(title(i), img)
    if i >= cnt:
        idx = 0

while True:
    key = cv2.waitKeyEx(0)
    display(idx)
    if key == 2555904 or key == 2490368 or key == 2424832 or key == 2621440:
        cv2.destroyWindow(title(idx))
    if key == ESC:
        break
    try:
        if key == 2555904 or key == 2490368:
            idx += 1
            display(idx)
            if cv2.waitKey(0) == key:
                cv2.destroyWindow(title(idx))
        elif key == 2424832 or key == 2621440:
            idx -= 1
            display(idx)
            if cv2.waitKey(0) == key:
                cv2.destroyWindow(title(idx))
    except KeyError:
        pass 
cv2.destroyAllWindows()