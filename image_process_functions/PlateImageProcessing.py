import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics
from collections import OrderedDict
class PlateImageProcessing:
    def __init__(self, imagePath):
        self.imagePath = imagePath
        self.GROUP_DISTANCE = 255

    def image_preprocessing(self):
        #convered to 8bit image for capturing ROI
        drew_image = cv2.imread(self.imagePath, cv2.IMREAD_COLOR)
        #raw plate image for fetching pixels' value (16bit image)
        plate_img = cv2.imread(self.imagePath,cv2.IMREAD_ANYDEPTH)
        # print("image shape : " + str(drew_image.shape))
        gray = cv2.cvtColor(drew_image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5),cv2.BORDER_DEFAULT)
        #   if pixel val > thresh, pixel val = maxval, otherwise = 0
        ret, thresh = cv2.threshold(blur, 255 * 0.60, 255,cv2.THRESH_BINARY_INV)
        return thresh,plate_img, drew_image

    # thresh,plate_img, drew_image = image_preprocessing("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif")
    def find_and_drew_contours(self,image, thresh):
        contours, hierarchies = cv2.findContours( thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        center_points = []
        for cnt in contours:
            # compute the center of the contour
            M = cv2.moments(cnt)
            res = np.zeros(image.shape[:2], np.uint8)
            if M['m00'] != 0 and M['m00'] >= 400 and M['m00'] <= 1200:
                cX = int(M['m10']/M['m00'])
                cY = int(M['m01']/M['m00'])
                center_points.append([cX,cY])
            # draw the contour and center of the shape on the image
                cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)
                cv2.circle(image, (cX, cY), 3, (0, 0, 0), -1)
        return center_points

    # contours_center_points = find_and_drew_contours(drew_image, thresh)
    # print("contours_center_points: " + str(len(contours_center_points)))


    def build_points_group(self,contours_center_points):
        visited = np.zeros(len(contours_center_points))
        GROUP_POINTS_DISTANCE = 88
        # a group: a pillar chip
        all_group_points = []
        center_points_len = len(contours_center_points)
        for i in range(center_points_len):
            group_points = []
            if visited[i] == 0:
                visited[i] = 1
                group_points.append(contours_center_points[i])
                for j in range(center_points_len):
                    if visited[j] == 0 and abs(contours_center_points[i][0] - contours_center_points[j][0]) < GROUP_POINTS_DISTANCE * 1.1 \
                    and abs(contours_center_points[i][1] - contours_center_points[j][1]) < GROUP_POINTS_DISTANCE * 1.1:
                        group_points.append(contours_center_points[j])
                        visited[j] = 1
            
            if len(group_points) > 0:            
                all_group_points.append(group_points)
        # print("number of group(pillar), it still contains noise: " + str(len(all_group_points)))
        return all_group_points



    def getAxisWithThreePoints(self,groupPoints):
        axis = [0] * 2
        for i in range(len(groupPoints) - 1):
            for j in range(i + 1 , len(groupPoints)):
                if (abs(groupPoints[i][0] - groupPoints[j][0]) < 30):
                    axis[1] = ((groupPoints[i][1] + groupPoints[j][1]) / 2)
                elif (abs(groupPoints[i][1] - groupPoints[j][1]) < 30):
                    axis[0] = ((groupPoints[i][0] + groupPoints[j][0]) / 2)

        return axis


    def filterNoise(self,groupPoints):#if group points > 4
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

    def get_theta(self,groupPoints):
        thetas = []
        for points in groupPoints:
            for i in range(0, len(points)):
                for j in range(i + 1, len(points)):
                    dy = abs(points[i][1] - points[j][1])
                    dx = abs(points[i][0] - points[j][0])
                    theta = math.atan2(dy, dx)
                    angle = math.degrees(theta)  # angle is in (-180, 180]
                    #88: it is the distance of two points in a group
                    #theta < angle(45 degrees)
                    if theta < 0.785398 and math.dist(points[i], points[j]) < (math.sqrt(2) - 0.2)* 88:
                        thetas.append(theta)
        theta = statistics.median(thetas)
        print("angle: " + str(angle))
        return theta


    def rotatePoint(self,point0, point1, imageShape, angle):
        #point1 rotate (angle) degrees counterclockwise around point0, for degree, if rotate clockwise, it should be negative
        #imageX: rows； 
        #imageShape: [y,x]
        #return new point position [x,y]
        imageX = imageShape[1]
        y1 = point1[1]
        x1 = point1[0]
        x2 = point0[0]
        y2 = point0[1]
        x1 = x1
        y1 = imageX - y1
        x2 = x2
        y2 = imageX - y2

        x = (x1 - x2)* math.cos(math.pi / 180.0 * angle) - (y1 - y2)*math.sin( math.pi / 180.0 * angle) + x2
        y = (x1 - x2)*math.sin(math.pi / 180.0 * angle) + (y1 - y2)*math.cos( math.pi / 180.0 * angle) + y2

        x = x
        y = imageX - y
        return [int(x),int(y)]

    # all_group_points = build_points_group(contours_center_points)

    def filter_group_points(self,all_group_points):
        groupWithFourOrThreePoints = []
        for groupPoints in all_group_points:
            if len(groupPoints) == 4 or len(groupPoints) == 3:
                groupWithFourOrThreePoints.append(groupPoints)
            if len(groupPoints) >= 5:
                points = self.filterNoise(groupPoints)
                if (points != None and len(points) >= 3):
                    groupWithFourOrThreePoints.append(points)
        # print("the number of groups with four or three points: " + str(len(groupWithFourOrThreePoints)))

        return groupWithFourOrThreePoints

    # groupWithFourOrThreePoints = filterGroupPoints(all_group_points)


    def get_group_center(self,all_group_points):
        groupCenters = []
        for group_points in all_group_points:
            if len(group_points) == 3:
                xy = self.getAxisWithThreePoints(group_points)
                #filter groupCenters those too close to the boundary （threshold =rectHalfSideLen）
                if xy[0] <= 80 or xy[0] >= 3270 or xy[1] <= 80 or xy[1] >= 2450:
                    continue
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
                if center[0] <= 20 or center[0] >= 3322 or center[1] <= 20 or center[1] >= 2502:
                    continue
                groupCenters.append(center)

        return groupCenters

    # groupCenters = get_group_center(groupWithFourOrThreePoints)

    def drew_points(drew_image, sortedGroupCenters):
        centerPointIdx = 0
        # rectHalfSideLen = 80
        rectHalfSideLen = 30
        yIdx = 'A'
        for groupCenters in sortedGroupCenters:
            xIdx = 1
            for point in groupCenters:
                cv2.circle(drew_image, (int(point[0]), int(point[1])), 8, (255, 153, 255), -1) 
                cv2.rectangle(drew_image, (int(point[0]) - rectHalfSideLen,int(point[1]) - rectHalfSideLen), (int(point[0]) + rectHalfSideLen,int(point[1]) + rectHalfSideLen),  (1, 190, 200), 1)
                cv2.putText(drew_image, str(yIdx) + str(xIdx),(int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)
                xIdx += 1
            yIdx = chr(ord(yIdx) + 1)      

    # GROUP_DISTANCE = 255

    def selfValidation(self, nameAndCoordDic):
        for i in range(ord('A'),ord('I')):
            for j in range(0,12):
                coord = str(chr(i))+str(j)
                coordRight = str(chr(i))+str(j + 1)
                coordDown = str(chr(i + 1))+str(j + 1)
                if coord in nameAndCoordDic.keys() and coordRight in nameAndCoordDic.keys():
                    coordRightVal = nameAndCoordDic[coordRight]
                    if abs(coordRightVal[0] - nameAndCoordDic[coord][0]) > self.GROUP_DISTANCE * 1.2:
                        return False
                if coord in nameAndCoordDic.keys() and coordDown in nameAndCoordDic.keys():
                    coordDownVal = nameAndCoordDic[coordDown]
                    if abs(coordDownVal[1] - nameAndCoordDic[coord][1]) > self.GROUP_DISTANCE * 1.2:
                        return False               
        return True


    def get_pillar_name_and_coord_dic(self, drew_image, groupCenters, corners, theta, positive_slope):
        nameAndCoordDic = {}
        rowsNumCheck = False
        colsNumCheck = False
        groupNameSet = set()
        group_name_for_sort_dic = {}
        yIdx = 'A'
        leftUpCorner = corners[0]
        # cv2.circle(drew_image, (int(corners[0][0]), int(corners[0][1])), 28, (255, 153, 255), -1) 
        # cv2.circle(drew_image, (int(corners[1][0]), int(corners[1][1])), 28, (255, 153, 255), -1) 
        # datumPoint = [(corners[0][0] + corners[1][0]) / 2,corners[0][1]]
        # cv2.circle(image, (int(datumPoint[0]), int(datumPoint[1])), 38, (255, 153, 255), -1) 
        # print("positive slope: " + positive_slope)
        # positive_slope = False
        for point in groupCenters:
            cv2.circle(drew_image, (int(point[0]), int(point[1])), 8, (255, 153, 255), -1) 
            dx = abs(point[0] - leftUpCorner[0])
            dy = point[1] - leftUpCorner[1]
            if positive_slope:
                # clockwise_rotate
                xIdx = int((dx + abs(dy) * math.tan(theta) + self.GROUP_DISTANCE / 2) / self.GROUP_DISTANCE) + 1
                y = int((dy - dx * math.tan(theta)  + self.GROUP_DISTANCE / 2 ) / self.GROUP_DISTANCE)
                
            else: 
                # anti_clockwise_rotate
                xIdx = int((dx- abs(dy) * math.tan(theta) + self.GROUP_DISTANCE / 2) / self.GROUP_DISTANCE)
                y = int((dy + dx * math.tan(theta)  + self.GROUP_DISTANCE / 2 ) / self.GROUP_DISTANCE) 

            #datum point : x: average x of  leftUpCorner and leftDownCorner    y : leftUpCorner  
            if xIdx >= 12:
                colsNumCheck = True
            if y >= 7:                                                                                                                                                                                                                                                                     
                rowsNumCheck = True            
            groupRowName = chr(ord(yIdx) + y)
            groupColName = xIdx
            groupName = str(chr(ord(yIdx) + y)) + str(xIdx)
            groupNameForSort = str(chr(ord(yIdx) + y)) + str(chr(xIdx + ord('A') - 1) )
            if (groupName in groupNameSet) or (groupRowName < 'A' or groupRowName > 'H') or (groupColName < 0 or groupColName > 12):
                cv2.putText(drew_image, str("Please retry,adjust image roration"),(600, 400), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 20)
                raise Exception('Please retry,adjust image roration')

            groupNameSet.add(groupName)
            group_name_for_sort_dic[groupNameForSort] = groupName

            if groupName in nameAndCoordDic.keys():
                cv2.putText(drew_image, str("Please retry,adjust image roration"),(600, 400), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 20)
                raise Exception('Please retry,adjust image roration')

            else:
                groupCentralPoint =  [int(point[0]), int(point[1])]
                nameAndCoordDic[groupName] =groupCentralPoint

            cv2.putText(drew_image, str(chr(ord(yIdx) + y) ) + str(xIdx),(int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)
            xIdx += 1
        if colsNumCheck == False or rowsNumCheck == False:
            cv2.putText(drew_image, str("Please retry, not enough chips"),(600, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 20)
        # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        group_name_for_sort_dic_keys = sorted(group_name_for_sort_dic.keys())

        name_and_coord_dic = self.sortDic(nameAndCoordDic,group_name_for_sort_dic_keys,group_name_for_sort_dic)
        # print(name_and_coord_dic)
        return name_and_coord_dic

    def sortDic(self,name_and_coord_dic, group_name_for_sort_dic_keys, group_name_for_sort_dic):
        sorted_dic = {}
        for group_name in group_name_for_sort_dic_keys:
            sorted_dic[group_name_for_sort_dic[group_name]] = name_and_coord_dic[group_name_for_sort_dic[group_name]]
        return sorted_dic


    def line_intersection(self,line1,line2):
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


    def find_corners(self,drew_image,groupPoints):  
        #find plate image corners
        line1 = [] #left line
        line2 = [] #top line
        line3 = []
        groupPoints.sort(key=lambda x:x[0]) # sorted by x axis
        leftPoint1 = groupPoints[0]
        leftPoint2 = groupPoints[2]
        line1.append(leftPoint1)
        line1.append(leftPoint2)
        # cv2.circle(drew_image, (int(leftPoint1[0]), int(leftPoint1[1])), 25, (255, 0, 0), -1) 
        # cv2.circle(drew_image, (int(leftPoint2[0]), int(leftPoint2[1])), 25, (255, 0, 0), -1) 
        groupPoints.sort(key=lambda x:x[1])
        topPoint1 = groupPoints[0]
        topPoint2 = groupPoints[2]
        bottomPoint1 = groupPoints[-1]
        bottomPoint2 = groupPoints[-3]
        # cv2.circle(drew_image, (int(topPoint1[0]), int(topPoint1[1])), 25, (255, 0, 0), -1) 
        # cv2.circle(drew_image, (int(topPoint2[0]), int(topPoint2[1])), 25, (255, 0, 0), -1) 
        # cv2.circle(drew_image, (int(bottomPoint1[0]), int(bottomPoint1[1])), 25, (255, 0, 0), -1) 
        # cv2.circle(drew_image, (int(bottomPoint2[0]), int(bottomPoint2[1])), 25, (255, 0, 0), -1) 
        line3.append(bottomPoint1)
        line3.append(bottomPoint2)
        line2.append(topPoint1)
        line2.append(topPoint2)

        #line1 left_line, line2 top_line, line3 bottom_line
        leftUpCorner = self.line_intersection(line1, line2)
        # print("leftUpCorner: " + str(leftUpCorner))
        leftDownCorner = self.line_intersection(line1, line3)
        #positive_slope 
        positive_slope = False

        if leftUpCorner[1] - topPoint2[1] < 0:
            positive_slope = True
        # print("is_positive_slope: " + str(positive_slope))

        # cv2.line(drew_image, (int(leftPoint1[0]),int(leftPoint1[1])), (int(leftPoint2[0]),int(leftPoint2[1])), (255,0,0), 8)
        # cv2.line(drew_image, (int(topPoint1[0]),int(topPoint1[1])), (int(topPoint2[0]),int(topPoint2[1])), (255,0,0), 8)
        # cv2.line(drew_image, (int(bottomPoint1[0]),int(bottomPoint1[1])), (int(bottomPoint2[0]),int(bottomPoint2[1])), (255,0,0), 8)

        # cv2.circle(drew_image, (int(leftUpCorner[0]), int(leftUpCorner[1])), 15, (255, 153, 0), -1) 

        return [leftUpCorner,leftDownCorner],positive_slope


    # corners, positive_slope = findCorners(drew_image,groupCenters)
    # theta = get_theta(groupWithFourOrThreePoints)
    # nameAndCoordDic = drewPointsPro(drew_image,groupCenters,corners,theta,positive_slope)


    def draw_chip_position(self,drew_image, nameAndCoordDic,positive_slope,theta):
        distance = 29
        radius = 11 # it will capture 439 pixels
        for name, groupCentralPoint in nameAndCoordDic.items():
            leftUpCornerX = groupCentralPoint[0] - 43
            leftUpCornerY = groupCentralPoint[1] - 43
            idx = 0

            for i in range(4):
                for j in range(4):
                    chipPosition = [int(leftUpCornerX + j * distance), int(leftUpCornerY + i * distance)]
                    cv2.circle(drew_image, (chipPosition[0], chipPosition[1]), radius, (51, 31, 218), 1) #blue circle
                    cv2.putText(drew_image, str(idx), (int(leftUpCornerX + j * distance), int(leftUpCornerY + i * distance)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)
                    idx += 1


    def getChipData(self,plate_img,centralPoint, radius):
        leftUpCorner = [centralPoint[0] - radius, centralPoint[1] - radius]
        rightDownCorner = [centralPoint[0] + radius, centralPoint[1] + radius]
        pixels = []
        for i in range(leftUpCorner[0], rightDownCorner[0]):
            for j in range(leftUpCorner[1], rightDownCorner[1]):
                if pow((i - centralPoint[0]),2) +  pow((j - centralPoint[1]),2) <= pow(radius,2):
                    pixels.append(plate_img[j,i])
        return statistics.median(pixels)


    def getChipCoordsInGroup(self,plate_img,pillarName,chipPositionIdxList,plateImgNameAndCoordDic,angle,isCounterClockwiseRotation):
        # chipPositionIdxList: from position image, determain which chip is used
        # get chip coordinates in plateImg with group name and chip indexs 
        distance = 29
        groupCentralPoint = plateImgNameAndCoordDic[pillarName]
        leftUpCornerX = groupCentralPoint[0] - 43
        leftUpCornerY = groupCentralPoint[1] - 43

        idx = 0
        chipIdxAndPosDic = {}
        for i in range(4):
            for j in range(4):
                if idx in chipPositionIdxList:
                    chipPosition = [int(leftUpCornerX + j * distance), int(leftUpCornerY + i * distance)]
                    if isCounterClockwiseRotation:
                        chipPosition = self.rotatePoint(groupCentralPoint, chipPosition, plate_img.shape,angle)
                    else:
                        chipPosition = self.rotatePoint(groupCentralPoint, chipPosition, plate_img.shape,-angle)

                    chipIdxAndPosDic[idx] =  chipPosition
                idx += 1
        return chipIdxAndPosDic




    def fetch_chip_data(self,plate_img,plateImgNameAndCoordDic,pillarName,chipPositionIdxList,radius, angle, isCounterClockwiseRotation,position_and_data_Dic):
        chipIdxAndPosDic = self.getChipCoordsInGroup(plate_img,pillarName, chipPositionIdxList, plateImgNameAndCoordDic, angle, isCounterClockwiseRotation)
        for idx, pos in chipIdxAndPosDic.items():
            data = self.getChipData(plate_img,pos,radius)
            position_and_data_Dic[str(pillarName) + '_' + str(idx)] = data


    def get_plate_img_data(self,plate_img,plateImgNameAndCoordDic, radius, angle, isCounterClockwiseRotation):
            position_and_data_Dic = {}
            for pillarName, _ in plateImgNameAndCoordDic.items():
                self.fetch_chip_data(plate_img,plateImgNameAndCoordDic,pillarName,[i for i in range(16)],radius, angle, isCounterClockwiseRotation,position_and_data_Dic)
            return position_and_data_Dic
    # get_plate_img_data(plate_img,nameAndCoordDic,12,math.degrees(theta), True)


# fig,ax = plt.subplots(1)
# ax.imshow(drew_image)
# plt.show()