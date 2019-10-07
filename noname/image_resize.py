import os
import numpy as np
import cv2
from PIL import Image

original_path = '/Users/halo/Documents/GitHub/senier/noname/training-images'
resized_path = '/Users/halo/Documents/GitHub/senier/noname/training-images'

file_list = os.listdir(original_path)
img_list = []

for item in file_list :
    if item.find('.JPEG') is not -1 :
        img_list.append(item)
img_list.sort()
total_image = len(img_list)
index = 0

for name in img_list :

    img = Image.open('%s%s'%(original_path, name))
    img_array = np.array(img)
    img_resize = cv2.resize(img_array, (240,240), interpolation = cv2.INTER_AREA)
    img = Image.fromarray(img_resize)
    img.save('%s%s.PNG'%(resized_path, name.split('.')[0]))

    print(name + '   ' + str(index) + '/' + str(total_image))
    index = index + 1
