import cv2
import matplotlib.pyplot as plt


class Position:
    def __init__(self, imagePath):
        self.imagePath = imagePath

    def getROI(self):
        image = cv2.imread(self.imagePath, cv2.IMREAD_COLOR)
        print("image shape : " + str(image.shape))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5),cv2.BORDER_DEFAULT)
        ret, thresh = cv2.threshold(blur, 255 * 0.24, 255,cv2.THRESH_BINARY_INV)
        contours, hierarchies = cv2.findContours( thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        return image,contours

    def getCenterPointsOfROI(self, image, contours):
        idx = 0
        centerPoints = []
        for cnt in contours:
            M = cv2.moments(cnt)
            if M['m00'] != 0 and M['m00'] >= 4000 and M['m00'] <= 24000 :#area is around 153*153=23409
                cX = int(M['m10']/M['m00'])
                cY = int(M['m01']/M['m00'])
                centerPoints.append([cX,cY])
                #draw the contour and center of the shape on the image
                cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)
                #draw center point
                cv2.circle(image, (cX, cY), 3, (0, 0, 0), -1)
                idx += 1
        return centerPoints

    def checkWithinDistance(p1, p2, dis):
        shorter = dis * 0.8
        longer = dis * 1.2
        if (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 >= shorter ** 2 or \
            (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 <= longer ** 2:
            return True
        return False

    def contains(self, centerPoints, currPoint):
        rectHalfSideLen = 75
        for point in centerPoints:
            if abs(point[0] - currPoint[0]) <= rectHalfSideLen * 0.3 and abs(point[1] - currPoint[1]) <= rectHalfSideLen * 0.3:
                return True
        return False

    def drawCenterPoints(self, image, centerPoints):
        centerPoints.sort(key=lambda x:x[0] + x[1]) # sorted by (x+y)
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
                    cv2.putText(image, str(idx),(y + rectHalfSideLen, x - rectHalfSideLen), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 3)
                    if self.contains(centerPoints,[x,y]):
                        cv2.rectangle(image, (int(x) - rectHalfSideLen,int(y) - rectHalfSideLen), (int(x) + rectHalfSideLen,int(y) + rectHalfSideLen),  (1, 190, 200), 5)
                        chipCenters[idx]=[x,y]
                    else :
                        cv2.rectangle(image, (int(x) - rectHalfSideLen,int(y) - rectHalfSideLen), (int(x) + rectHalfSideLen,int(y) + rectHalfSideLen),  (255, 0, 0), 5)
                        missingCenterPoints.append(idx)
                    cv2.circle(image, (x, y), 8, (255, 255, 0), -1)
                idx += 1

        return chipCenters,fourCornersDic,missingCenterPoints




p = Position("C:/Users/Vibrant/Desktop/openCV/positions/image0.tif")
image,contours = p.getROI()
centerPoints = p.getCenterPointsOfROI(image, contours)
chipCenters,fourCornersDic,missingCenterPoints = p.drawCenterPoints(image,centerPoints)
print("ROI: " + str(chipCenters))
print("fourCornersDic " + str(fourCornersDic))
print("missingCenterPoints " + str(missingCenterPoints))
fig,ax = plt.subplots(1)
ax.imshow(image)
plt.show()
