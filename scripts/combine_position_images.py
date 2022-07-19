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

def drawIndex(image,distance):
    x = 76
    y = 186
    for i in range(ord('A'),ord('I')):
        x = 78
        for j in range(1,13):
            coord = str(chr(i))+str(j)
            cv2.putText(image, coord, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)
            x = x + distance
        y = y + distance
    return image
image = drawIndex(vtich,205)
fig,ax = plt.subplots(1)
ax.imshow(image)
plt.show()