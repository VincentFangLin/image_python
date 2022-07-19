import cv2
import numpy as np 
import matplotlib.pyplot as plt

import statistics

# def printPixelValWithThresh(src, threshold):
#     shape = src.shape #rows is y in imageJ
#     for i in range(rows):
#         for j in range(cols):
#             k = src[i,j]
#             # if j == 519 and i == 207:
#             #     print(k) 
#             #     break
#             if k > threshold:
#                 print("X: " + str(j) + " Y: " + str(i) + " Value: " + str(k))




# image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img0.tif", cv2.IMREAD_COLOR)
image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif",cv2.IMREAD_ANYDEPTH)
# src = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img0.tif", cv2.IMREAD_COLOR)

shape = image.shape
print(shape)
print("=================")
print(image[167][209])
print(image[209][167])# image[y][x]



# [176, 200]
# [176, 201]
# [176, 202]
# [176, 203]
# [176, 204]
# cv2.circle(image, (207,165), 18, (255, 153, 255), 6) 
# cv2.circle(src, (170,207), 11, (255, 153, 255), 3) 
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
plt.show()
# print(src[0,0,0])

# def printPixels(img):
#     shape = img.shape
#     for i in range(0, shape[0]):
#         for j in range(0, shape[1]):
#             # for k in range(0, shape[2]):
#             if img[i,j] > 200 and img[i,j] < 500:
#                 print(img[i,j])



# printPixels(image)

# # gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# # 寻找轮廓
# bimg, contours, hier = cv2.findContours(src, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)













# print(type(src))
# print(src.shape)

# print(src)
# retaval,thresh_image =cv2.threshold(src, 65535 * 0.8, 65535, cv2.THRESH_BINARY) #将大于thresh的值设置为255. 将小于thresh的值设置为0.
# print(src.shape)
# printPixelValWithThresh(gray, 100)

# # print(thresh_image.shape)
# # image_8bit = np.uint8(thresh_image * 255)
# # print(image_8bit)

# # _,binarized = cv2.threshold(image_8bit, threshold_level, 255, cv2.THRESH_BINARY)
# # print(binarized.shape)

# # im2, contours, hierarchy = cv2.findContours(binarized, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # img = cv2.cvtColor(thresh_image, cv2.COLOR_BGR2GRAY)

# # contours, hierarchy = cv2.findContours(image=img, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
# # # blank = np.zeros(thresh.shape)
# # image_copy = src.copy()

# # cv2.drawContours(blank, contours, -1,
# #                 (255, 0, 0), 1)
 

# # img8 = (src/256).astype('uint8')
# # print(img8[207,519])
# circ = plt.Circle((150, 150), 20, color='r')
# fig,ax = plt.subplots(1)
# ax.set_aspect('equal')

# # plt.figure()
# ax.imshow(src)
# ax.add_patch(circ)

# plt.show()
# # cv2.circle(thresh_image, (20,20), radius=5, color=(255,0,0), thickness=-1)

# # # _, contours, hierarchy = cv2.findContours(img8, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# # cv2.imshow('image',thresh_image)


# # cv2.waitKey(0) # waits until a key is pressed
# # cv2.destroyAllWindows() # destroys the window showing image




# # x, y, z = np.where(image==(255,255,255))
# # points = zip(x,y)
# # print(list(points))