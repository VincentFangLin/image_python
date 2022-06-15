
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

ret, thresh = cv2.threshold(blur, 200, 255,
                           cv2.THRESH_BINARY_INV)
print(thresh)
contours, hierarchies = cv2.findContours(
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
blank = np.zeros(thresh.shape[:2],
                 dtype='uint8')
print(blank)
cv2.drawContours(blank, contours, -1,
                (255, 0, 0), 1)
 
cv2.imwrite("Contours.png", blank)
# center points we will be using the moments() 
for i in contours:
    M = cv2.moments(i)
    if M['m00'] != 0:
        # 空间矩
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.drawContours(image, [i], -1, (0, 255, 0), 2)
        cv2.circle(image, (cx, cy), 2, (255, 0, 0), -1) 
        # cv2.putText(image, "center", (cx - 20, cy - 20),
        #            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    # print(f"x: {cx} y: {cy}")

fig,ax = plt.subplots(1)
ax.imshow(image)
plt.show()
# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

