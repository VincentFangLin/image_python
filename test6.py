
# Python code to read image
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
            if k == threshold :
                print("X: " + str(j) + " Y: " + str(i) + " Value: " + str(k))
# To read image from disk, we use
# cv2.imread function, in below method,
image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img1.tif", cv2.IMREAD_COLOR)
print(type(image))
print(image.shape)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray.shape)
blur = cv2.GaussianBlur(gray, (5, 5),
                       cv2.BORDER_DEFAULT)
# retval, dst = cv.threshold( src, thresh, maxval, type[, dst] ) 

ret, thresh = cv2.threshold(blur, 255 * 0.85, 255,
                           cv2.THRESH_BINARY_INV)
# Initialize empty list
lst_intensities = []

# For each list of contour points...
def accessImagePixels(contours):
    for i in range(len(contours)):
        # Create a mask image that contains the contour filled in
        cimg = np.zeros_like(image)
        cv2.drawContours(cimg, contours, i, color=255, thickness=-1)

        # Access the image pixels and create a 1D numpy array then add to list
        pts = np.where(cimg == 255)
        # print("pts")
        # print(pts)
        lst_intensities.append(image[pts[0], pts[1]])
contours, hierarchies = cv2.findContours( 
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
print(contours[0])

accessImagePixels(contours)
print("===============")
print(len(lst_intensities))
print(lst_intensities[0])
print(len(lst_intensities[0]))


fig,ax = plt.subplots(1)
ax.imshow(image)
plt.show()