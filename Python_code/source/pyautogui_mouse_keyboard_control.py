# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:39:38 2020

@author: Fam
"""
#%%

# pip install pyautogui 설치
import pyautogui as pag
import time

# 마우스 커서 좌표
pag.position()

# 마우스 이동
pag.moveTo(511,14) # x, y, 시간

pag.click() # 마우스 클릭

time.sleep(1) # 창이 뜰때까지 기다리기

pag.moveTo(700,418)

pag.click()

time.sleep(1)

pag.typewrite('python') # 단어 입력 

pag.typewrite(['enter']) # [] 안에 쓰면 키보드 위의 버튼 누르는 것과 같음.

#%%
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