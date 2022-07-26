import cv2
import numpy as np 
import matplotlib.pyplot as plt

import statistics



image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif",cv2.IMREAD_ANYDEPTH)
shape = image.shape
print(shape)
print("=================")
print(image[167][209])
print(image[209][167])# image[y][x]

def getMedian(centralPoint, radius):
    leftUpCorner = [centralPoint[0] - radius, centralPoint[1] - radius]
    rightDownCorner = [centralPoint[0] + radius, centralPoint[1] + radius]
    pixels = []
    for i in range(leftUpCorner[0], rightDownCorner[0]):
        for j in range(leftUpCorner[1], rightDownCorner[1]):
            if pow((i - centralPoint[0]),2) +  pow((j - centralPoint[1]),2) <= pow(radius,2):
                # print([i,j])
                pixels.append(image[j,i])
    print("number of pixels: " + str(len(pixels)))
    print(pixels)
    print("median pixel value: " + str(statistics.median(pixels)))


getMedian((170,207), 11)

fig,ax = plt.subplots(1)
ax.imshow(image)
#   (block=False)

print("--------")

plt.show()
