#%%
# Load Library
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import pyramid_reduce
#%%
os.chdir('C:/Users/ebool/study/source/OpenCV_super_resolution')
base_path = '..\..\image\celeba-dataset'
img_base_path = os.path.join(base_path, 'img_align_celeba')
target_img_path = os.path.join(base_path, 'processed')
#%%
eval_list = np.loadtxt(os.path.join(base_path, 'list_eval_partition.csv'),
                       dtype=str,
                       delimiter=',',
                       skiprows=1)
#%%
img_sample = cv2.imread(os.path.join(img_base_path, 
                                     eval_list[0][0]))

h, w, _ = img_sample.shape

# 정사각형 이미지로 crop 해준다.
crop_sample = img_sample[int((h-w)/2):int(-(h-w)/2), :] 

# 이미지를 4배만큼 축소하고 normalize 한다.
resized_sample = pyramid_reduce(crop_sample, 
                                downscale=4,
                                multichannel=True) # 컬러채널 허용

pad = int((crop_sample.shape[0] - resized_sample.shape[0]) / 2)

padded_sample = cv2.copyMakeBorder(resized_sample,
                                   top=pad,
                                   bottom=pad,
                                   left=pad,
                                   right=pad,
                                   borderType=cv2.BORDER_CONSTANT,
                                   value=(0,0,0))

print(crop_sample.shape, padded_sample.shape)

fig, ax = plt.subplots(1,4,figsize=(12,5))

ax=ax.ravel()

ax[0].imshow(img_sample)
ax[1].imshow(crop_sample)
ax[2].imshow(resized_sample)
#ax[2].imshow(cv2.resize(resized_sample,dsize=(45, 45)))
ax[3].imshow(padded_sample)
#%%
downscale = 4
n_train = 162770
n_val = 19867
n_test = 19962

for i, e in enumerate(eval_list):
    filename, ext = os.path.splitext(e[0])
    
    img_path = os.path.join(img_base_path, e[0])
    
    img = cv2.imread(img_path)
    
    h, w, _ = img.shape
    
    crop = img[int((h-w)/2):int(-(h-w)/2), :]
    crop = cv2.resize(crop, dsize=(176,176))
    resized = pyramid_reduce(crop, downscale=downscale, multichannel=True)
    
    norm = cv2.normalize(crop.astype(np.float64), None, 0, 1, cv2.NORM_MINMAX)
    
    if int(e[1]) == 0: # Train
        np.save(os.path.join(target_img_path, 'x_train', filename + '.npy'), resized)
        np.save(os.path.join(target_img_path, 'y_train', filename + '.npy'), norm)
    elif int(e[1]) == 1: # Validation
        np.save(os.path.join(target_img_path, 'x_val', filename + '.npy'), resized)
        np.save(os.path.join(target_img_path, 'y_val', filename + '.npy'), norm)
    elif int(e[1]) == 2: # Test
        np.save(os.path.join(target_img_path, 'x_test', filename + '.npy'), resized)
        np.save(os.path.join(target_img_path, 'y_test', filename + '.npy'), norm)        
#%%               
        