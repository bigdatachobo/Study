import cv2
import sys
import numpy as np

# 흑백이미지로 변환
def grayscale(img): 
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Canny 알고리즘
def canny(img, low_threshold, high_threshold): 
    return cv2.Canny(img, low_threshold, high_threshold)

# 가우시안 필터
def gaussian_blur(img, kernel_size): 
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

# ROI 셋팅
def region_of_interest(img, vertices, color3=(255,255,255), color1=255): 

    mask = np.zeros_like(img) # mask = img와 같은 크기의 빈 이미지
    
    if len(img.shape) > 2: # Color 이미지(3채널)라면 :
        color = color3
    else: # 흑백 이미지(1채널)라면 :
        color = color1
        
    # vertices에 정한 점들로 이뤄진 다각형부분(ROI 설정부분)을 color로 채움 
    cv2.fillPoly(mask, vertices, color)
    
    # 이미지와 color로 채워진 ROI를 합침
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image

# 선 그리기
def draw_lines(img, lines, color=[0, 0, 255], thickness=2): 
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

# 허프 변환-직선
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap): 
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), 
                                minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)

    return line_img

# 두 이미지 operlap 하기
def weighted_img(img, initial_img, α=1, β=1., λ=0.): 
    return cv2.addWeighted(initial_img, α, img, β, λ)


# 동영상 불러오기
cap = cv2.VideoCapture('videos/solidWhiteRight.mp4') 
#cap = cv2.VideoCapture("videos/road5.mp4")

if not cap.isOpened():
    print('Can not cap opened!')
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print('can not read!')
        sys.exit()

    h, w = frame.shape[:2] # 이미지 높이, 너비
    print(frame.shape)    
    gray_img = grayscale(frame) #1.흑백이미지로 변환
    
    blur_img = gaussian_blur(gray_img, 3) #2.Blur 효과
        
    canny_img = canny(blur_img, 70, 210) #3.Canny edge 알고리즘

    vertices = np.array([[(50,h),(w/2-45, h/2+60), 
                        (w/2+45, h/2+60), (w-50,h)]], dtype=np.int32)
    ROI_img = region_of_interest(canny_img, vertices) #4.ROI 설정

    hough_img = hough_lines(ROI_img, 1, 1 * np.pi/180, 30, 10, 20) #5.허프 변환

    result = weighted_img(hough_img, frame) # 원본 이미지에 검출된 선 overlap
    cv2.imshow('canny_img',canny_img) # 결과 이미지 출력
    cv2.imshow('ROI_img',ROI_img) # 결과 이미지 출력
    cv2.imshow('hough_img',hough_img) # 결과 이미지 출력
    cv2.imshow('result',result) # 결과 이미지 출력


    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()