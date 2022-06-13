import cv2
import numpy as np 
import matplotlib.pyplot as plt

max_row = 0
max_col = 0
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

                


src = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img1.tif",cv2.IMREAD_ANYDEPTH)
print(type(src))
print(src.shape)
print(src)
num_rows, num_cols = src.shape
visit = np.zeros([num_rows,  num_cols])
print(visit)

count = 0
for i in range(num_rows):
    for j in range(num_cols):
        if src[i][j] > 60000 and visit[i][j] == 0:
            max_row = i
            max_col = j
            flood(src, visit, i, j, 60000, num_cols, num_cols)
            count += 1
            print("=====================" + str(count))
            print(max_row)
            print(max_col)




def printNP(src):
    rows,cols = src.shape #rows is y in imageJ
    for i in range(rows):
        for j in range(cols):
            if visit[i][j] > 0 :
                print(src[i][j])


retaval,thresh_image =cv2.threshold(src, 65535 * 0.8, 65535, cv2.THRESH_BINARY) #将大于thresh的值设置为255. 将小于thresh的值设置为0.
circ = plt.Circle((150, 150), 20, color='r')
fig,ax = plt.subplots(1)
ax.set_aspect('equal')
# plt.figure()
ax.imshow(src)
ax.add_patch(circ)
plt.show()
