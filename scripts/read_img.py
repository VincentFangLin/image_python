from turtle import distance
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics
from skimage.io import imread_collection
import glob

# image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif", cv2.IMREAD_COLOR)

#your path 
folderPath = 'C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/*.tif'

#creating a collection with the available images
# col = imread_collection(folderPath)


def loadImages(folderPath):
    collection = imread_collection(folderPath)
    print(len(collection))
    return collection

collection = loadImages(folderPath)
# print(collection)
# print(len(collection))
print(collection[0])



#images 16bit -> 8bit
# images = [cv2.imread(file) for file in glob.glob('C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/*.tif')]
# print(len(images))
# print(images[0])
# print(images[1])
# fig,ax = plt.subplots(1)
# ax.imshow(images[0])
# plt.show()