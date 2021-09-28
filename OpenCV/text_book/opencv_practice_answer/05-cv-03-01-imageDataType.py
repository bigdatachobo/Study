import cv2 

img1 = cv2.imread('images/cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('images/cat.bmp', cv2.IMREAD_COLOR)

print(f'차원: {img1.ndim}')
print(f'차원크기: {img1.shape}')
print(f'전체 데이터 개수: {img1.size}')
print(f'영상 데이터 타입: {img1.dtype}')
print('------------')
print(f'차원: {img2.ndim}')
print(f'차원크기: {img2.shape}')
print(f'전체 데이터 개수: {img2.size}')
print(f'영상 데이터 타입: {img2.dtype}')