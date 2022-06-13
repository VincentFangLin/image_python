import cv2
import numpy as np 
import matplotlib.pyplot as plt
def printPixelValWithThresh(src, threshold):
    rows,cols = src.shape #rows is y in imageJ
    for i in range(rows):
        for j in range(cols):
            k = src[i,j]
            # if j == 519 and i == 207:
            #     print(k) 
            #     break
            if k > threshold:
                print("X: " + str(j) + " Y: " + str(i) + " Value: " + str(k))

src = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img1.tif",cv2.IMREAD_ANYDEPTH)
print(type(src))
print(src.shape)
print(src)
retaval,thresh_image =cv2.threshold(src, 65535 * 0.8, 65535, cv2.THRESH_BINARY) #将大于thresh的值设置为255. 将小于thresh的值设置为0.
circ = plt.Circle((150, 150), 20, color='r')
fig,ax = plt.subplots(1)
ax.set_aspect('equal')
# plt.figure()
ax.imshow(src)
ax.add_patch(circ)
plt.show()
