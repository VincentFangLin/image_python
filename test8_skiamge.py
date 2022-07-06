import cv2
import numpy as np
import matplotlib.pyplot as plt

from skimage import segmentation

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

image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img1.tif", cv2.IMREAD_COLOR)
print("image shape: " + str(image.shape))
msk = np.zeros(image.shape, np.uint8)
print("msk shape: " +  str(msk.shape))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("gray shape: " +  str(gray.shape))

# cv2.bilateralFilter(image, 5, 200, 5)
# im2 = cv2.GaussianBlur(image,(5,5),0)
blur = cv2.GaussianBlur(gray, (5, 5),
                       cv2.BORDER_DEFAULT)
# retval, dst = cv.threshold( src, thresh, maxval, type[, dst] ) 

ret, thresh = cv2.threshold(blur, 100, 65535,
                           cv2.THRESH_BINARY_INV)
boundaries = segmentation.find_boundaries(thresh, mode='thick').astype(np.uint8)
# printPixelValWithThresh(boundaries,  65535 * 0.85)
# print(boundaries)
fig,ax = plt.subplots(1)
ax.imshow(boundaries)
plt.show()