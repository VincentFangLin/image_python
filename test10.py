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

def selfValidation():
    for i in range(ord('A'),ord('I')):
        for j in range(0,12):
            print(str(chr(i))+str(j))


selfValidation()