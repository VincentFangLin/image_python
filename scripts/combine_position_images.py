import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
htich_tuple = ()

def convert_index(index):#index to coord
    r = int(index / 12)
    c = index % 12
    coord = str(chr(r + ord('A')))+str(c + 1)
    return coord
for r in range(0,8):
    images = ()
    for i in range(0,12):
        index = 12 * r  + i
        coord = convert_index(index)
        image = mpimg.imread('processed_position_images/' + 'combined_image_' + str(coord) +'.jpeg')
        image = cv2.resize(image, None, fx=0.2, fy=0.2)
        images = images + (image,)
    htich = np.hstack(images)
    htich_tuple = htich_tuple + (htich,)
vtich = np.vstack(htich_tuple)


def drawIndex(image,distance):
    x = 76
    y = 186
    for i in range(ord('A'),ord('I')):
        x = 78 
        for j in range(1,13):
            coord = str(chr(i))+str(j)
            cv2.putText(image, coord, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)
            x = x + distance * 2
        y = y + distance * 2
    return image
image = drawIndex(vtich,205)
fig,ax = plt.subplots(1)
ax.imshow(image)
plt.show()