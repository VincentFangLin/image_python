import cv2
import numpy as np 
import matplotlib.pyplot as plt

max_row = 0
max_col = 0
MAX_PIXEL_VALUE = 65535
def printPixelValWithThresh(src, threshold):
    rows,cols = src.shape #rows is y in imageJ
    for i in range(rows):
        for j in range(cols):
            k = src[i,j]
            # if j == 519 and i == 207:
            #     print(k) 
            #     break
            if k > threshold:
                print("X: " + str(j) + " Y: " + str(i) + " Value: " + str(k))

def flood(src, visit, i , j, threshold, rows, cols):
    if (i < 0 or i >= rows or j < 0 or j >= cols or visit[i][j] == 1 or src[i][j] < threshold):
        return
    visit[i][j] = 1
    global max_row
    global max_col
    if i > max_row:
        max_row = i
    if j > max_col:
        max_col = j
    flood(src, visit, i + 1, j, threshold, rows, cols)
    flood(src, visit, i - 1, j, threshold, rows, cols)
    flood(src, visit, i , j + 1, threshold, rows, cols)
    flood(src, visit, i , j - 1, threshold, rows, cols)

                


src = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img0.tif",cv2.IMREAD_ANYDEPTH)
print(type(src))
print(src.shape)
# print(src)
num_rows, num_cols = src.shape
visit = np.zeros([num_rows,  num_cols])
# print(visit)

count = 0
center_points = []
circs = []
prev_i = 0
prev_j = 0
for i in range(num_rows):
    for j in range(num_cols):
        if src[i][j] > MAX_PIXEL_VALUE * 0.9 and visit[i][j] == 0:
            max_row = i
            max_col = j
            flood(src, visit, i, j, MAX_PIXEL_VALUE * 0.9, num_cols, num_cols)
            count += 1
            # print("=====================" + str(count))
            # print(max_row)
            # print(max_col)
            row_ave = (i + max_row) / 2
            col_ave = (j + max_col) / 2
            # [1290.0, 286.5], [1277.5, 290.5]
            # [1278.0, 546.0], [1461.0, 547.5],
            center_points.append([col_ave, row_ave])
            # circ = plt.Circle(( col_ave, row_ave), 3, color='r')
            # circs.append(circ)


center_points.sort(key=lambda x:x[0])
center_points_count = len(center_points)
for i in range(1, center_points_count):
    if (abs(center_points[i][0] - center_points[i - 1][0]) < 20.0 and abs(center_points[i][1] - center_points[i - 1][1]) < 20.0):
        print("-----------")
        print("continue" + str(center_points[i-1][0]))
        print("continue" + str(center_points[i-1][1]))
        print("continue" + str(center_points[i][0]))
        print("continue" + str(center_points[i][1]))
        print("-----------")
    else :
        circ = plt.Circle(( center_points[i][0], center_points[i][1]), 3, color='r')
        circs.append(circ)



print("center points number:" + str(len(center_points)))
print("circs number:" + str(len(circs)))

print(center_points)


# def printNP(src):
#     rows,cols = src.shape #rows is y in imageJ
#     for i in range(rows):
#         for j in range(cols):
#             if visit[i][j] > 0 :
#                 print(src[i][j])



retaval,thresh_image =cv2.threshold(src, MAX_PIXEL_VALUE * 0.8, MAX_PIXEL_VALUE, cv2.THRESH_BINARY) #将大于thresh的值设置为255. 将小于thresh的值设置为0.
# circ1 = plt.Circle((150, 150), 20, color='r')
# circ2 = plt.Circle((250, 150), 20, color='r')
# circ3 = plt.Circle((350, 150), 20, color='r')

# circs.append(circ1)
# circs.append(circ2)
# circs.append(circ3)
# print(circs)
fig,ax = plt.subplots(1)
ax.set_aspect('equal')
# plt.figure()
for c in circs:
    ax.add_patch(c)

ax.imshow(src)
plt.show()
