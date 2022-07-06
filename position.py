import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics

image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/position1.tif", cv2.IMREAD_COLOR)
# image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif", cv2.IMREAD_COLOR)
# angle = 0
print(type(image))  
print("image shape : ")
print(image.shape)                                                                                                                                                                     
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5),
                       cv2.BORDER_DEFAULT)

ret, thresh = cv2.threshold(blur, 255 * 0.23, 255,
                           cv2.THRESH_BINARY_INV)


contours, hierarchies = cv2.findContours( 
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)



print(len(contours))

def drawContours(contours):
    idx = 0
    center_points = []
    for cnt in contours:
        M = cv2.moments(cnt)
        # res = np.zeros(image.shape[:2], np.uint8)
        # M['m00'] : area
        if M['m00'] != 0 and M['m00'] >= 4000 and M['m00'] <= 24000 :#area is around 153*153=23409
            cX = int(M['m10']/M['m00'])
            cY = int(M['m01']/M['m00'])
            center_points.append([cX,cY])
        # draw the contour and center of the shape on the image
            cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)
            #画中心点
            cv2.circle(image, (cX, cY), 3, (0, 0, 0), -1)
            cv2.putText(image, str(idx),(cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)

            #画轮廓
            idx += 1
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)  # cv.boxPoints(rect) for OpenCV 3.x 获取最小外接矩形的4个顶点
            box = np.int0(box)
            # print("四个顶点坐标为;", box)
            cv2.drawContours(image, [box], -1, (0, 0, 255), 3)
            # cv2.drawContours(res, [box], -1, 255,5)

drawContours(contours)
fig,ax = plt.subplots(1)
ax.imshow(image)
plt.show()
