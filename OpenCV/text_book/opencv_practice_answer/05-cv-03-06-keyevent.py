import cv2

img = cv2.imread('images/cat.bmp', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)

while True:
    keycode = cv2.waitKey()
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv2.imshow('image', img)
    elif keycode == 27:
        break
    
cv2.destroyAllWindows()