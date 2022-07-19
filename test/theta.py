import math
import statistics
from xml.etree.ElementTree import PI
theta = math.atan2(2, 2)
angle = math.degrees(theta)  # angle is in (-180, 180]
print(theta)
print(angle)


#假设图像的宽度x高度为col x row,图像中某个像素P(x1,y1)，
# 绕某个像素点Q(x2,y2)旋转θ角度后,则该像素点的新坐标位置为(x, y)，其计算公式为：

def rotatePoint(point0, point1, imageShape, angle):
    #point1 rotate (angle) degrees counterclockwise around point0 
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
    print("x: " + str(x))
    print("y: " + str(y))
    return [x,y]

rotatePoint([0,0],[10,10],[2532,3352],45)

# def points(m1,m2,n1,n2):
#     # q1 = math.Point(m1,m2)
#     # q2 = math.Point(n1,n2)
#     len12 = ((m1-n1)**2+(m2-n2)**2)**0.5
#     n1 = int(len12/10)
#     t12x = (10*(n1-m1))/len12
#     t12y = (10*(n2-m2))/len12
#     lis1 = []
#     lis1.append([m1,m2])
#     for i in range (1,3):
#             a = [m1+i*t12x,m2+i*t12y]
#             lis1.append(a)
#     print(lis1)


# points(0,0,100,100)