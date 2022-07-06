from turtle import distance
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics

image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/positions/image0.tif", cv2.IMREAD_COLOR)
# image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif", cv2.IMREAD_COLOR)
# angle = 0
print(type(image))  
print("image shape : ")
print(image.shape)                                                                                                                                                                     
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5),
                       cv2.BORDER_DEFAULT)

ret, thresh = cv2.threshold(blur, 255 * 0.24, 255,
                           cv2.THRESH_BINARY_INV)


contours, hierarchies = cv2.findContours( 
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)



print(len(contours))

def drawContours(contours):
    idx = 0
    centerPoints = []
    for cnt in contours:
        M = cv2.moments(cnt)
        # res = np.zeros(image.shape[:2], np.uint8)
        # M['m00'] : area
        if M['m00'] != 0 and M['m00'] >= 4000 and M['m00'] <= 24000 :#area is around 153*153=23409
            cX = int(M['m10']/M['m00'])
            cY = int(M['m01']/M['m00'])
            centerPoints.append([cX,cY])
        # draw the contour and center of the shape on the image
            cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)
            #画中心点
            cv2.circle(image, (cX, cY), 3, (0, 0, 0), -1)
            # cv2.putText(image, str(idx),(cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)

            #画轮廓
            idx += 1
            rect = cv2.minAreaRect(cnt)
            # box = cv2.boxPoints(rect)  # cv.boxPoints(rect) for OpenCV 3.x 获取最小外接矩形的4个顶点
            # box = np.int0(box)
            # print("四个顶点坐标为;", box)
            # cv2.drawContours(image, [box], -1, (0, 0, 255), 3)
            # cv2.drawContours(res, [box], -1, 255,5)

    print(centerPoints)
    # centerPoints.sort(key=lambda x:x[0]) # sorted by x axis
    print(centerPoints)
    return centerPoints




def checkWithinDistance(p1, p2, dis):
    shorter = dis * 0.8
    longer = dis * 1.2
    if (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 >= shorter ** 2 or \
        (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 <= longer ** 2:
        return True
    return False
     

def contains(centerPoints, currPoint):
    rectHalfSideLen = 75
    for point in centerPoints:
        if abs(point[0] - currPoint[0]) <= rectHalfSideLen * 0.3 and abs(point[1] - currPoint[1]) <= rectHalfSideLen * 0.3:
            print(abs(point[0] - currPoint[0]))
            return True
    return False

def drawCenterPoints(centerPoints):
    centerPoints.sort(key=lambda x:x[0] + x[1]) # sorted by (x+y)
    print("======sorted======")
    print(centerPoints)
    leftUpCorner = centerPoints[0]
    distance = 196
    rectHalfSideLen = 75
    missingCenterPoints = []
    fourCornersDic = {}
    chipCenters = {}
    xStart = leftUpCorner[0]
    yStart = leftUpCorner[1]
    idx = 0
    for i in range(4):
        for j in range(4):
            x = xStart + distance * i
            y = yStart + distance * j
            if idx == 0:
                fourCornersDic["leftUpCorner"]=[x,y]
                cv2.putText(image, str(idx),(y + rectHalfSideLen, x - rectHalfSideLen), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)
                cv2.rectangle(image, (int(x) - rectHalfSideLen,int(y) - rectHalfSideLen), (int(x) + rectHalfSideLen,int(y) + rectHalfSideLen),  (1, 190, 200), 5)
            elif idx == 3:
                fourCornersDic["rightUpCorner"]=[x,y]
                cv2.putText(image, str(idx),(y + rectHalfSideLen, x - rectHalfSideLen), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)
                cv2.rectangle(image, (int(x) - rectHalfSideLen,int(y) - rectHalfSideLen), (int(x) + rectHalfSideLen,int(y) + rectHalfSideLen),  (1, 190, 200), 5)
            elif idx == 12:
                fourCornersDic["leftDownCorner"]=[x,y]
                cv2.putText(image, str(idx),(y + rectHalfSideLen, x - rectHalfSideLen), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)
                cv2.rectangle(image, (int(x) - rectHalfSideLen,int(y) - rectHalfSideLen), (int(x) + rectHalfSideLen,int(y) + rectHalfSideLen),  (1, 190, 200), 5)
            elif idx == 15:
                fourCornersDic["rightDownCorner"]=[x,y]
                cv2.putText(image, str(idx),(y + rectHalfSideLen, x - rectHalfSideLen), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)
                cv2.rectangle(image, (int(x) - rectHalfSideLen,int(y) - rectHalfSideLen), (int(x) + rectHalfSideLen,int(y) + rectHalfSideLen),  (1, 190, 200), 5)
            else:
                # if idx
                cv2.putText(image, str(idx),(y + rectHalfSideLen, x - rectHalfSideLen), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)
                if contains(centerPoints,[x,y]):
                # cv2.rectangle(image, ( (int(x - rectHalfSideLen),int(y - rectHalfSideLen)), (int(x + rectHalfSideLen),int(y + rectHalfSideLen)),  (1, 190, 200), 1))
                    cv2.rectangle(image, (int(x) - rectHalfSideLen,int(y) - rectHalfSideLen), (int(x) + rectHalfSideLen,int(y) + rectHalfSideLen),  (1, 190, 200), 5)
                    chipCenters[idx]=[x,y]
                else :
                    print("==============")
                    cv2.rectangle(image, (int(x) - rectHalfSideLen,int(y) - rectHalfSideLen), (int(x) + rectHalfSideLen,int(y) + rectHalfSideLen),  (255, 0, 0), 5)
                    missingCenterPoints.append([x,y])
                cv2.circle(image, (x, y), 8, (255, 255, 0), -1)
            idx += 1

    return chipCenters,fourCornersDic,missingCenterPoints

    
centerPoints = drawContours(contours)

chipCenters,fourCornersDic,missingCenterPoints = drawCenterPoints(centerPoints)
print("chipCenters " + str(chipCenters))
print("fourCornersDic " + str(fourCornersDic))
print("missingCenterPoints " + str(missingCenterPoints))

fig,ax = plt.subplots(1)
ax.imshow(image)
plt.show()
