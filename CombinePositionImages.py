from turtle import distance
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class CombinePositionImages:
    def __init__(self):
        self.distance = 205
    def convert_index(self,index):#index to coord
        r = int(index / 12)
        c = index % 12
        coord = str(chr(r + ord('A')))+str(c + 1)
        return coord
    def getCombinedImage(self):
        htich_tuple = ()
        for r in range(0,8):
            images = ()
            for i in range(0,12):
                index = 12 * r  + i
                coord = self.convert_index(index)
                image = mpimg.imread('processed_position_images/' + 'combined_image_' + str(coord) +'.jpeg')
                image = cv2.resize(image, None, fx=0.2, fy=0.2)
                images = images + (image,)
            htich = np.hstack(images)
            htich_tuple = htich_tuple + (htich,)
        vtich_image = np.vstack(htich_tuple)
        return vtich_image
    def drawIndex(self,image):
        x = 76
        y = 186
        for i in range(ord('A'),ord('I')):
            x = 78 
            for j in range(1,13):
                coord = str(chr(i))+str(j)
                cv2.putText(image, coord, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)
                x = x + self.distance * 2
            y = y + self.distance * 2
        return image
    
# cpi = CombinePositionImages()
# new_iamge = cpi.getCombinedImage()
# image = cpi.drawIndex(new_iamge)
# # image = drawIndex(vtich,205)
# fig,ax = plt.subplots(1)
# ax.imshow(image)
# plt.show()
