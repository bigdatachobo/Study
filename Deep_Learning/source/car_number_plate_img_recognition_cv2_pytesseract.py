# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:29:57 2020

@author: Fam
"""
#%%
# Library Loading
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
import os
os.chdir('C:/Users/Fam/Downloads/Python/study/source')
cv2.__version__
#%%
# Read Input Image
img_ori = cv2.imread('../image/bmw_car_number.jpg')

height, width, channel = img_ori.shape

plt.figure(figsize=(12,10))
plt.imshow(img_ori, cmap='gray')
#%%
# Convert Image to Grayscale
# 이미지 프로세싱하기 쉽게 그레이스케일로 바꿔준다.

gray = cv2.cvtColor(img_ori, 
                    cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(12,10))
plt.imshow(gray, cmap='gray')
#%%
# Maximize Contrast(Optional)
structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT,
                                               (3,3))

imgTopHat = cv2.morphologyEx(gray, 
                             cv2.MORPH_TOPHAT, 
                             structuringElement)

imgBlackHat = cv2.morphologyEx(gray, 
                               cv2.MORPH_BLACKHAT, 
                               structuringElement)

imgGrayscalePlusTopHat = cv2.add(gray, imgTopHat)

gray = cv2.subtract(imgGrayscalePlusTopHat, imgBlackHat)

plt.figure(figsize=(12,10))
plt.imshow(gray, cmap='gray')
#%%
# Adaptive Thresholding

# 노이즈 제거 위해 가우시안 블러 사용
img_blurred = cv2.GaussianBlur(gray,
                               ksize=(5,5),
                               sigmaX=0)

img_thresh = cv2.adaptiveThreshold(img_blurred,
                                    maxValue=255.0,
                                    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    thresholdType=cv2.THRESH_BINARY_INV,
                                    blockSize=19,
                                    C=9)

plt.figure(figsize=(12, 10))
plt.imshow(img_thresh, cmap='gray')
#%%
# Find Contours
# 아래의 경우 2018년 openCV 버전에선 _,contours,_ 형식이었지만
# 2020년 openCV 버전에선 contours,_ 처럼 바뀜
# 출처: https://www.youtube.com/watch?v=PpTl7xxGXh4 맨 밑의 댓글에 질문 참조함
contours, _ = cv2.findContours(img_thresh, 
                               mode=cv2.RETR_LIST, 
                               method=cv2.CHAIN_APPROX_SIMPLE)

temp_result = np.zeros((height, width, channel), 
                       dtype=np.uint8)

cv2.drawContours(temp_result, 
                 contours=contours, 
                 contourIdx=-1, # -1 -> 전체 컨투어를 적용하겠다는 의미
                 color=(255, 255, 255))

plt.figure(figsize=(12, 10))
plt.imshow(temp_result)
#%%
# Prepare Data

temp_result = np.zeros((height, width, channel), dtype=np.uint8)
contours_dict = []

for contour in contours:
    x,y,w,h = cv2.boundingRect(contour) # 윤곽선을 감싸는 사각형 구함
    cv2.rectangle(temp_result, # 사각형 그리기
                  pt1=(x,y),
                  pt2=(x+w, y+h),
                  color=(255,255,255),
                  thickness=2)
    # insert to dict
    contours_dict.append({'contour':contour,
                          'x':x,
                          'y':y,
                          'w':w,
                          'h':h,
                          'cx':x+(w/2), # 사각형 x 중심좌표 
                          'cy':y+(h/2)}) # 사각형 y 중심좌표

plt.figure(figsize=(12,10))    
plt.imshow(temp_result, cmap='gray')
#%%
# Select Candidates by Char Size

MIN_AREA = 80
MIN_WIDTH, MIN_HEIGHT = 2, 8
MIN_RATIO, MAX_RATIO = 0.25, 1.0

possible_contours = [] # 거른 contours를 따로 저장

cnt = 0
for d in contours_dict:
    area = d['w']*d['h']
    ratio = d['w']/d['h']
    
    if area > MIN_AREA \
    and d['w'] > MIN_WIDTH and d['h'] > MIN_HEIGHT\
    and MIN_RATIO < ratio < MAX_RATIO:
            d['idx'] = cnt # 인덱스도 같이 저장해줌.
            cnt += 1
            possible_contours.append(d)
# visualize possible contours
temp_result = np.zeros((height, width, channel), dtype=np.uint8)            

for d in possible_contours:
    cv2.rectangle(temp_result,
                  pt1=(d['x'], d['y']),
                  pt2=(d['x']+d['w'], d['y']+d['h']),
                  color=(255,255,255),
                  thickness=2)

plt.figure(figsize=(12,10))    
plt.imshow(temp_result, cmap='gray')
#%%
# Select Candidates by Arrangement of Contours

MAX_DIAG_MULTIPLYER = 5 # 사각형 사이 거리가 대각선 길이의 5배 안에 들어와 있어야함
MAX_ANGLE_DIFF = 12.0 # 사각형 중심 사이의 각도가 12도 이내여야함.
MAX_AREA_DIFF = 0.5 # 사각형 면적 차이가 0.5배 이하여야함.
MAX_WIDTH_DIFF = 0.8 # 너비의 차이가 0.8배 이하여야함.
MAX_HEIGHT_DIFF = 0.2 # 높이 차이가 0.2배 이항여야함.
MIN_N_MATCHED = 3 # 조건을 만족하는 사각형 갯수가 3개 이상이어야함.

def find_chars(contour_list):
    matched_result_idx = [] #  최종결과물의 인덱스값 저장
    
    for d1 in contour_list:
        matched_contours_idx = []
        for d2 in contour_list:
            if d1['idx'] == d2['idx']: # 인덱스끼리 비교 --> 만약 같다면 비교할 필요 없으므로 continue로 넘겨버림
                continue

            dx = abs(d1['cx'] - d2['cx'])
            dy = abs(d1['cy'] - d2['cy'])

            diagonal_length1 = np.sqrt(d1['w'] ** 2 + d1['h'] ** 2)

            distance = np.linalg.norm(np.array([d1['cx'], d1['cy']]) - np.array([d2['cx'], d2['cy']]))
            if dx == 0: # 예외처리
                angle_diff = 90 # 90도
            else:
                angle_diff = np.degrees(np.arctan(dy / dx))
            area_diff = abs(d1['w'] * d1['h'] - d2['w'] * d2['h']) / (d1['w'] * d1['h'])
            width_diff = abs(d1['w'] - d2['w']) / d1['w']
            height_diff = abs(d1['h'] - d2['h']) / d1['h']

            if distance < diagonal_length1 * MAX_DIAG_MULTIPLYER \
            and angle_diff < MAX_ANGLE_DIFF and area_diff < MAX_AREA_DIFF \
            and width_diff < MAX_WIDTH_DIFF and height_diff < MAX_HEIGHT_DIFF:
                matched_contours_idx.append(d2['idx'])

        # append this contour
        matched_contours_idx.append(d1['idx'])

        if len(matched_contours_idx) < MIN_N_MATCHED: # 네모의 갯수가 3보다 작으면 기각함
            continue

        matched_result_idx.append(matched_contours_idx)

        unmatched_contour_idx = []
        for d4 in contour_list:
            if d4['idx'] not in matched_contours_idx:
                unmatched_contour_idx.append(d4['idx'])
                            
        unmatched_contour = np.take(possible_contours, unmatched_contour_idx)
                            # np.take(a, idx) --> a에서 idx와 같은 인덱스의 값만 추출
        # recursive
        recursive_contour_list = find_chars(unmatched_contour) # 함수로 다시 돌려본다.
        
        for idx in recursive_contour_list:
            matched_result_idx.append(idx)

        break

    return matched_result_idx
    
result_idx = find_chars(possible_contours)

matched_result = []
for idx_list in result_idx:
    matched_result.append(np.take(possible_contours, idx_list))

# visualize possible contours
temp_result = np.zeros((height, width, channel), dtype=np.uint8)

for r in matched_result:
    for d in r:
#         cv2.drawContours(temp_result, d['contour'], -1, (255, 255, 255))
        cv2.rectangle(temp_result, 
                      pt1=(d['x'], d['y']), 
                      pt2=(d['x']+d['w'], d['y']+d['h']), 
                      color=(255, 255, 255), 
                      thickness=2)

plt.figure(figsize=(12, 10))
plt.imshow(temp_result, cmap='gray')
#%%
# Rotate Plate Images
# 동영상 13분 53초

PLATE_WIDTH_PADDING = 1.3
PLATE_HEIGHT_PADDING = 1.5
MIN_PLATE_RATIO = 3
MAX_PLATE_RATIO = 10

plate_imgs = []
plate_infos = []

for i, matched_chars in enumerate(matched_result):
    sorted_chars = sorted(matched_chars, key=lambda x: x['cx'])
    
    plate_cx = (sorted_chars[0]['cx'] + sorted_chars[-1]['cx']) / 2
    plate_cy = (sorted_chars[0]['cy'] + sorted_chars[-1]['cy']) / 2 
    
    plate_width = (sorted_chars[-1]['x'] + sorted_chars[-1]['w'] - sorted_chars[0]['x'])*PLATE_WIDTH_PADDING
    
    sum_height = 0
    for d in sorted_chars:
        sum_height += d['h']
        
    plate_height = int(sum_height / len(sorted_chars)*PLATE_HEIGHT_PADDING)        
    
    triangle_height = sorted_chars[-1]['cy'] - sorted_chars[0]['cy']
    triangle_hypotenus = np.linalg.norm(np.array([sorted_chars[0]['cx'], sorted_chars[0]['cy']])- # 첫번호판과 마지막 번호판 사이의 거리 구하기
                                        np.array([sorted_chars[-1]['cx'], sorted_chars[-1]['cy']]))
    
    angle = np.degrees(np.arcsin(triangle_height / triangle_hypotenus))
    
    rotation_matrix = cv2.getRotationMatrix2D(center=(plate_cx, plate_cy), # 로테이션 이미지 구한다.
                                              angle=angle,
                                              scale=1.0)
    
    img_rotated = cv2.warpAffine(img_thresh,  # 이미지를 수평으로 돌려준다.
                                 M=rotation_matrix,
                                 dsize=(width, height))
    
    img_cropped = cv2.getRectSubPix(img_rotated, # 회전된 이미지에서 원하는 부분만 잘라낸다.
                                    patchSize=(int(plate_width),int(plate_height)),
                                    center=(int(plate_cx), int(plate_cy)))
    
    if img_cropped.shape[1] / img_cropped.shape[0] < MIN_PLATE_RATIO or img_cropped.shape[1] / img_cropped.shape[0] < MIN_PLATE_RATIO > MAX_PLATE_RATIO:
        continue
    
    plate_imgs.append(img_cropped)
    plate_infos.append({'x': int(plate_cx - plate_width / 2),
                        'y': int(plate_cy - plate_height / 2),
                        'w': int(plate_width),
                        'h': int(plate_height)})
    
    plt.subplot(len(matched_result), 1, i+1)
    plt.imshow(img_cropped, cmap='gray')    

#%%
# Another Thresholding to Find Chars
    
longest_idx, longest_text = -1, 0
plate_chars = []

for i, plate_img in enumerate(plate_imgs):
    plate_img = cv2.resize(plate_img, 
                           dsize=(0, 0), 
                           fx=1.6, 
                           fy=1.6)
    
    _, plate_img = cv2.threshold(plate_img, 
                                 thresh=0.0, 
                                 maxval=255.0, 
                                 type=cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # find contours again (same as above)
    contours, _ = cv2.findContours(plate_img, 
                                   mode=cv2.RETR_LIST, 
                                   method=cv2.CHAIN_APPROX_SIMPLE)
    
    plate_min_x, plate_min_y = plate_img.shape[1], plate_img.shape[0]
    plate_max_x, plate_max_y = 0, 0

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        
        area = w * h
        ratio = w / h

        if area > MIN_AREA \
        and w > MIN_WIDTH and h > MIN_HEIGHT \
        and MIN_RATIO < ratio < MAX_RATIO:
            if x < plate_min_x:
                plate_min_x = x
            if y < plate_min_y:
                plate_min_y = y
            if x + w > plate_max_x:
                plate_max_x = x + w
            if y + h > plate_max_y:
                plate_max_y = y + h
                
    img_result = plate_img[plate_min_y:plate_max_y, plate_min_x:plate_max_x]
    
    img_result = cv2.GaussianBlur(img_result, 
                                  ksize=(3, 3), 
                                  sigmaX=0)
    
    _, img_result = cv2.threshold(img_result, 
                                  thresh=0.0, 
                                  maxval=255.0, 
                                  type=cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    img_result = cv2.copyMakeBorder(img_result, # 이미지에 패딩을 준다.( 빈곳 채움)
                                    top=10, 
                                    bottom=10, 
                                    left=10, 
                                    right=10, 
                                    borderType=cv2.BORDER_CONSTANT, 
                                    value=(0,0,0)) # 검정색으로 빈곳 채운다.

    chars = pytesseract.image_to_string(img_result, 
                                        lang='kor', 
                                        config='--psm 7 --oem 0')
    
    result_chars = ''
    has_digit = False
    for c in chars:
        if ord('가') <= ord(c) <= ord('힣') or c.isdigit():
            if c.isdigit():
                has_digit = True
            result_chars += c
    
    print(result_chars)
    plate_chars.append(result_chars)

    if has_digit and len(result_chars) > longest_text:
        longest_idx = i

    plt.subplot(len(plate_imgs), 1, i+1)
    plt.imshow(img_result, cmap='gray')
#%%    
# Result
    
info = plate_infos[longest_idx]    
chars = plate_chars[longest_idx]

print(chars)

img_out = img_ori.copy()

cv2.rectangle(img_out,
              pt1=(info['x'], info['y']),
              pt2=(info['x'] + info['w'], info['y'] + info['h']),
              color=(255,0,0),
              thickness=2)

cv2.imwrite(chars + '.jpg', img_out)

plt.figure(figsize=(12, 10))
plt.imshow(img_out)
#%%












