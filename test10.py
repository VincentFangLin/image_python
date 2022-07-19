# # cv2.threshold(src, thresh, maxval, type[, dst])，返回值为retval, dst
# # 其中：
# # src是灰度图像
# # thresh是起始阈值
# # maxval是最大值
# # type是定义如何处理数据与阈值的关系。有以下几种：
# # 选项	                       像素值>thresh	其他情况
# # cv2.THRESH_BINARY_INV          	0	        maxval
# import math
# # Return the arc tangent of (y,x) in radians:
# theta = math.atan2(3, -2)
# print(theta)
# # angle = math.degrees(theta)  # angle is in (-180, 180]
# # print(angle)
# print(math.tan(theta))
# # atan2 方法返回一个 -pi 到 pi 之间的数值，表示点 (x, y) 对应的偏移角度。这是一个逆时针角度，
# # 以弧度为单位，正X轴和点 (x, y) 与原点连线之间。函数接受的参数：先传递 y 坐标，然后是 x 坐标。out


# groupNameSet = set()
# groupNameSet.add(1)
# groupNameSet.add(2)
# groupRowName = 'B'
# # (groupRowName < 'A' or groupRowName > 'Z') or (groupColName < 0 or groupColName > 9)


# print(groupRowName > 'A')

# dict = {
#   "brand": ["a"],
#   "model": "Mustang",
#   "year": 1964
# }
# if 'brand' in dict.keys():
#     print(dict["brand"])
# else:
#     print(dict["year"])
# # a['b'] = 3
# print(dict["b"])

# def selfValidation():
#     for i in range(ord('A'),ord('I')):
#         for j in range(0,12):
#             print(str(chr(i))+str(j))

# def checkWithinDistance(p1, p2, dis):
#     shorter = dis * 0.8
#     longer = dis * 1.2
#     edge = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
#     if edge >= shorter ** 2 or edge <= longer ** 2:
#         return True
#     return False
# print(checkWithinDistance([0,0],[2,2],30))



# def groupCenters(centerPoints):
#     innerPoints = []
#     outterPoints = []
#     innerDis = 190
#     ouuterDis = 580
#     visited = np.zeros(len(centerPoints))
#     centerPointsLen = len(centerPoints)
#     for i in range(centerPointsLen):
#         currPoint = centerPoints[i]
#         if visited[i] == 0:
#             for j in range(centerPointsLen):
#                 if visited[j] == 0 and (((abs(currPoint[0] - centerPoints[j][0]) > ouuterDis * 0.8 \
#                 and abs(currPoint[0] - centerPoints[j][0]) < ouuterDis * 1.2)) or (abs(currPoint[1] - centerPoints[j][1]) > ouuterDis * 0.8 \
#                 and abs(currPoint[1] - centerPoints[j][1]) < ouuterDis * 1.2)):
#                     if visited[i] == 0:
#                         outterPoints.append(currPoint)
#                     visited[i] = 1
#                     outterPoints.append(centerPoints[j])
#                     visited[j] = 1
#     for i in range(len(visited)):
#         if visited[i] == 0:
#             innerPoints.append(centerPoints[i])
#             visited[i] = 1
#     print("----")   
#     print(outterPoints)
#     print(innerPoints)
#     return outterPoints,innerPoints
# # groupCenters(centerPoints)
# from datetime import datetime


# # proposedDatetime = datetime.strptime('2022-07-15 10:35:50', '%y-%m-%d %H:%M:%S').date()
# a = datetime('2022-07-15 16:05:02.524076')
# currResponseTime = datetime.now()

# # diff = currResponseTime - proposedDatetime
# print(currResponseTime)
import numpy as np

arr1 = np.array([[1,3], [2,4] ])
arr2 = np.array([[1,4], [2,6] ])
arr = ()
arr = arr + (arr1,)
res = np.hstack((arr))
 
print (res)