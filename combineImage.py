import cv2
import numpy as np
import matplotlib.pyplot as plt
from PositionImageProcessing import PositionImageProcessing
import matplotlib.image as mpimg
htich_tuple = ()
for r in range(1,9):
    images = ()
    for i in range(1,13):
        image = mpimg.imread('processed_position_images/' + 'combined_image_' + str(12 * (r - 1) + i) +'.jpeg')
        image = cv2.resize(image, None, fx=0.1, fy=0.1)
        images = images + (image,)
    htich = np.hstack(images)
    htich_tuple = htich_tuple + (htich,)
vtich = np.vstack(htich_tuple)

# img1 = cv2.resize(img1, None, fx=0.02, fy=0.02)    #为了完整显示，缩小一倍

cv2.putText(vtich, 'A1', (int(500), int(500)), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 0), 3)


fig,ax = plt.subplots(1)
ax.imshow(vtich)
plt.show()