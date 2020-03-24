# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:10:37 2020

@author: Fam
"""
#%%
# pip install mss : 스크린샷 패키지 설치
# pip install opencv-python

import mss
import cv2
import pyautogui as pag
import numpy as np
import time

first_button=[515,241]
single_button = [500, 272]
double_button = [500, 310]

single_icon_pos={'left':500,
                 'top':372, #272
                 'width':111,
                 'height':34}

double_icon_pos={'left':500,
                 'top':266, #272
                 'width':111,
                 'height':68}

with mss.mss() as sct:
    pag.move(515,354)
    pag.click()
    time.sleep(.1)
    single_img = np.array(sct.grab(single_icon_pos))[:,:,:3]
    
    
    time.sleep(.1)
    pag.move(515,241)
    pag.click()
    time.sleep(.1)
    double_img = np.array(sct.grab(double_icon_pos))[:,:,:3]
    
    cv2.imshow('single_img', single_img)
    cv2.imshow('double_img', double_img)
    cv2.waitKey(1)
    
# 마우스 포인터 좌표 출력
while True:
    x,y=pag.position()
    position_str='X: ' + str(x) + ' Y: ' + str(y)
    print(position_str)

def mouse_click(x,y):
    pag.moveTo(x, y)
    pag.click()
    time.sleep(.01)

position=[(515,242),(564,318),(559,608),(650,606)]
    
x=[515,564,559,650]#,514,561,562,651]
y=[242,318,608,606]#,242,291,612,605]

while True:
    for i,j in zip(x,y):
        mouse_click(i,j)    