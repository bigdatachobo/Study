import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 컬러 영상 불러오기
src = cv2.imread('images/candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
h, w, _ = src.shape
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

# RGB 색 평면 분할
b_plane, g_plane, r_plane = cv2.split(src)
# b_plane = src[:, :, 0]
# g_plane = src[:, :, 1]
# r_plane = src[:, :, 2]
print('b_plane.shape:', b_plane.shape)  # b_plane.shape: (480, 640)

# 채널을 변형한 뒤에 다시 합치거나 순서를 변경하면 원본 이미지와 다른 색상으로 표현
# m = cv2.merge((r_plane, g_plane, b_plane))
# cv2.imshow('m', m)
# 채널을 변형한 뒤에 R/G/B 색상으로 표현 하려면
zero = np.zeros((h, w, 1), dtype=np.uint8)
b_plane = cv2.merge((b_plane, zero, zero))
g_plane = cv2.merge((zero, g_plane, zero))
r_plane = cv2.merge((zero, zero, r_plane))

#원본 색상을 표현하기 위해서 plt에서는 cv2.cvtColor를 적용해 줘야한다.
src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
b_plane = cv2.cvtColor(b_plane, cv2.COLOR_BGR2RGB)
g_plane = cv2.cvtColor(g_plane, cv2.COLOR_BGR2RGB)
r_plane = cv2.cvtColor(r_plane, cv2.COLOR_BGR2RGB)

plt.subplot(221), plt.axis('off'), plt.imshow(src), plt.title('src')
plt.subplot(222), plt.axis('off'), plt.imshow(b_plane), plt.title('b_plane')
plt.subplot(223), plt.axis('off'), plt.imshow(g_plane), plt.title('g_plane')
plt.subplot(224), plt.axis('off'), plt.imshow(r_plane), plt.title('r_plane')
plt.show()
