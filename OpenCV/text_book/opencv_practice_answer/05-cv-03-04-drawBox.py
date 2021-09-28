import cv2

#color 설정
black_c = (0,0,0)
white_c = (255,255,255)
blue_c = (255,0,0)
red_c = (0,0,255)
green_c = (0,255,0)

img = cv2.imread('images/person1.jpg', cv2.IMREAD_COLOR)

cv2.rectangle(img, (80,100,160,200), green_c, thickness=2, lineType=None, shift=None)
cv2.rectangle(img, (270,80,170,215), green_c, thickness=2, lineType=None, shift=None)  


text = "korean girl"
cv2.putText(img, text, (80, 90), cv2.FONT_HERSHEY_DUPLEX, 0.8, green_c, 1, cv2.LINE_AA)

text = "korean boy"
cv2.putText(img, text, (270, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8,
green_c, 1, cv2.LINE_AA)

cv2.imshow('Identity Person',img)

cv2.waitKey()
cv2.destroyAllWindows()