import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img0.tif", cv2.IMREAD_COLOR)
print(type(image))
print("image shape : ")
print(image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5),
                       cv2.BORDER_DEFAULT)
# retval, dst = cv.threshold( src, thresh, maxval, type[, dst] ) 

ret, thresh = cv2.threshold(blur, 255 * 0.60, 255,
                           cv2.THRESH_BINARY_INV)
# print(thresh)
contours, hierarchies = cv2.findContours( 
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
idx = 0
center_points = []

for cnt in contours:
    # compute the center of the contour
    M = cv2.moments(cnt)
    res = np.zeros(image.shape[:2], np.uint8)

    if M['m00'] != 0 and M['m00'] >= 400 and M['m00'] <= 1200:
        # 空间矩
        # print("area "+str(M['m00']))
        # perimeter = cv2.arcLength(i,True)
        # print("perimeter " + str(perimeter))
        cX = int(M['m10']/M['m00'])
        cY = int(M['m01']/M['m00'])
        center_points.append([cX,cY])

    # draw the contour and center of the shape on the image
        cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)
        #画中心点
        cv2.circle(image, (cX, cY), 3, (0, 0, 0), -1)
        #画轮廓
        # cv2.putText(image, "C" + str(idx), (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        idx += 1
    
        rect = cv2.minAreaRect(cnt)
        # print("中心坐标：", rect[0])
        # print("宽度：", rect[1][0])
        # print("长度：", rect[1][1])
        # print("旋转角度：", rect[2])
        box = cv2.boxPoints(rect)  # cv.boxPoints(rect) for OpenCV 3.x 获取最小外接矩形的4个顶点
        box = np.int0(box)
        # print("四个顶点坐标为;", box)
        draw_img = cv2.drawContours(image, [box], -1, (0, 0, 255), 3)
        cv2.drawContours(res, [box], -1, 255,5)
        # print ("Area: " + str(cv2.contourArea(cnt)), "Mean: " + str(float(cv2.meanStdDev(thresh, mask=res)[0])))

visited = np.zeros(len(center_points))

GROUP_POINTS_DISTANCE = 88
all_group_points = []
def buildPointsGroup(center_points, visited):
    center_points_len = len(center_points)
    for i in range(center_points_len):
        group_points = []
        if visited[i] == 0:
            visited[i] = 1
            group_points.append(center_points[i])
            for j in range(center_points_len):
                if visited[j] == 0 and abs(center_points[i][0] - center_points[j][0]) < GROUP_POINTS_DISTANCE * 1.1 \
                and abs(center_points[i][1] - center_points[j][1]) < GROUP_POINTS_DISTANCE * 1.1:
                    group_points.append(center_points[j])
                    visited[j] = 1
        
        if len(group_points) > 0:            
            all_group_points.append(group_points)


def getAxisWithThreePoints(groupPoints):
    axis = [0] * 2
    for i in range(len(groupPoints) - 1):
        for j in range(i + 1 , len(groupPoints)):
            if (abs(groupPoints[i][0] - groupPoints[j][0]) < 30):
                axis[1] = ((groupPoints[i][1] + groupPoints[j][1]) / 2)
            elif (abs(groupPoints[i][1] - groupPoints[j][1]) < 30):
                axis[0] = ((groupPoints[i][0] + groupPoints[j][0]) / 2)

    return axis

    
def filterNoise(groupPoints):#if group points > 4
    points = []
    for i in range(len(groupPoints) - 1):
        firstPoint = groupPoints[i]
        points.append(firstPoint)
        for j in range(i + 1, len(groupPoints)):
            nextPoint = groupPoints[j]
            if (abs(firstPoint[0] - nextPoint[0]) < 20 and abs(firstPoint[1] - nextPoint[1]) > 50) \
            or (abs(firstPoint[0] - nextPoint[0]) > 50 and abs(firstPoint[1] - nextPoint[1]) < 20):
                points.append(nextPoint)
        if len(points) >= 3:
            return points
        if len(points) < 3:
            points = []

    return points






buildPointsGroup(center_points, visited)

groupWithFourOrThreePoints = []
def filterGroupPoints(all_group_points):
    for groupPoints in all_group_points:
        if len(groupPoints) == 4 or len(groupPoints) == 3:
            groupWithFourOrThreePoints.append(groupPoints)
        if len(groupPoints) >= 5:
            points = filterNoise(groupPoints)

            if (points != None and len(points) >= 3):
                groupWithFourOrThreePoints.append(points)
  



filterGroupPoints(all_group_points)

print("the number of groups: " + str(len(all_group_points)))
groupCenters = []


def getGroupCenter(all_group_points):
    for group_points in all_group_points:
        if len(group_points) == 3:
            xy = getAxisWithThreePoints(group_points)
            groupCenters.append(xy)
        else:

            num = len(group_points)
            x = 0
            y = 0
            
            for point in group_points:
                x += point[0]
                y += point[1]
            center = []
            center.append(x / num)
            center.append(y / num)
            groupCenters.append(center)

centerPointIdx = 0
rectHalfSideLen = 80

def drewPoints(sortedGroupCenters):
    yIdx = 'A'
    for groupCenters in sortedGroupCenters:
        xIdx = 1
        for point in groupCenters:
            cv2.circle(image, (int(point[0]), int(point[1])), 8, (255, 153, 255), -1) 
            cv2.rectangle(image, (int(point[0]) - rectHalfSideLen,int(point[1]) - rectHalfSideLen), (int(point[0]) + rectHalfSideLen,int(point[1]) + rectHalfSideLen),  (1, 190, 200), 5)
            cv2.putText(image, str(yIdx) + str(xIdx),(int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)
            xIdx += 1
        yIdx = chr(ord(yIdx) + 1)            

getGroupCenter(groupWithFourOrThreePoints)
#points in xAxis: 12
#points in yAxis: 8

GROUP_DISTANCE = 260

def drewPointsPro(groupCenters, leftUpCorner):
    rowsNumCheck = False
    colsNumCheck = False
    print("leftUpCorner " + str(leftUpCorner))
    yIdx = 'A'
    for point in groupCenters:
        cv2.circle(image, (int(point[0]), int(point[1])), 8, (255, 153, 255), -1) 
        cv2.rectangle(image, (int(point[0]) - rectHalfSideLen,int(point[1]) - rectHalfSideLen), (int(point[0]) + rectHalfSideLen,int(point[1]) + rectHalfSideLen),  (1, 190, 200), 5)
        xIdx = int((point[0] -  leftUpCorner[0] + GROUP_DISTANCE / 2)/ GROUP_DISTANCE)
        y = int((point[1] - leftUpCorner[1] + GROUP_DISTANCE / 2 )/ GROUP_DISTANCE) 
        if xIdx >= 11:
            colsNumCheck = True
        if y >= 7:
            rowsNumCheck = True            
        cv2.putText(image, str(chr(ord(yIdx) + y) ) + str(xIdx),(int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)
        xIdx += 1
    # if colsNumCheck == False or rowsNumCheck == False:
        # cv2.putText(image, str("Please retry, not enough chips"),(600, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 20)


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def findLeftUpCorner(groupPoints):
    print("---------------------------------")
    print(groupCenters)     
    groupPoints.sort(key=lambda x:x[0])
    firstPX = groupPoints[0]
    secondPX = groupPoints[1]
    groupPoints.sort(key=lambda x:x[1])
    firstPY = groupPoints[0]
    secondPY = groupPoints[1]
    line1 = []
    line2 = []
    line1.append(firstPX)
    line1.append(secondPX)
    line2.append(firstPY)
    line2.append(secondPY)
    print(firstPX)
    print(secondPX)
    print("=========================")
    print(firstPY)
    print(secondPY)
    print(line1)
    print(line2)

    intersectionPoint = line_intersection(line1, line2)
    cv2.line(image, (int(firstPX[0]),int(firstPX[1])), (int(intersectionPoint[0]),int(intersectionPoint[1])), (255,0,0), 8)
    cv2.line(image, (int(secondPY[0]),int(secondPY[1])), (int(intersectionPoint[0]),int(intersectionPoint[1])), (255,0,0), 8)
    return intersectionPoint
    # groupSortedByY = [i for i in groupPoints.sort(key=lambda x:x[1])]
    # print(groupSortedByX)
    # print(groupSortedByY)


LeftUpCorner = findLeftUpCorner(groupCenters)
cv2.circle(image, (int(LeftUpCorner[0]), int(LeftUpCorner[1])), 15, (255, 153, 0), -1) 



# sortedGroupCenters = []
# rowA = [] # < 367
# rowB = [] # < 636
# rowC = [] # < 895
# rowD = [] # < 1153
# rowE = [] # < 1412
# rowF = [] # < 1670
# rowG = [] # < 1928
# rowH = [] # 
# arrangedCenterPoints = [ [0]*2 for i in range(96)]

# def sortCenterPoints(groupCenters):
#     for center in groupCenters:
#         y = center[1]
#         if y < 374:
#             rowA.append(center)
#         elif y < 636:
#             rowB.append(center)
#         elif y < 895:
#             rowC.append(center)
#         elif y < 1153:
#             rowD.append(center)
#         elif y < 1412:
#             rowE.append(center)
#         elif y < 1670:
#             rowF.append(center)
#         elif y < 1928:     
#             rowG.append(center)
#         else:
#             rowH.append(center)
#     rowA.sort(key=lambda x:x[0])
#     rowB.sort(key=lambda x:x[0])
#     rowC.sort(key=lambda x:x[0])
#     rowD.sort(key=lambda x:x[0])
#     rowE.sort(key=lambda x:x[0])
#     rowF.sort(key=lambda x:x[0])
#     rowG.sort(key=lambda x:x[0])
#     rowH.sort(key=lambda x:x[0])
#     sortedGroupCenters.append(rowA)
#     sortedGroupCenters.append(rowB)
#     sortedGroupCenters.append(rowC)
#     sortedGroupCenters.append(rowD)
#     sortedGroupCenters.append(rowE)
#     sortedGroupCenters.append(rowF)
#     sortedGroupCenters.append(rowG)
#     sortedGroupCenters.append(rowH)

# sortCenterPoints(groupCenters)
# print("number of groupCenters " + str(len(groupCenters)))
# # drewPoints(sortedGroupCenters)
drewPointsPro(groupCenters,LeftUpCorner)



fig,ax = plt.subplots(1)
ax.imshow(image)
plt.show()
# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# I think the easiest is to create a mask for each contour, and then use the mean function to get the average color inside it.

# If you create an empty one channel image the same size as your input, you can use drawContours to fill the area of
#  the contour with 255. That is the mask to use with the mean function. Do this for each candidate, 
# and there you go.