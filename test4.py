
# Python code to read image
import cv2
import numpy as np
import matplotlib.pyplot as plt
def printPixelValWithThresh(src, threshold):
    rows,cols = src.shape #rows is y in imageJ
    for i in range(rows):
        for j in range(cols):
            k = src[i,j]
            # if j == 519 and i == 207:
            #     print(k) 
            #     break
            if k == threshold :
                print("X: " + str(j) + " Y: " + str(i) + " Value: " + str(k))
# To read image from disk, we use
# cv2.imread function, in below method,
image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img1.tif", cv2.IMREAD_COLOR)
print(type(image))
print(image.shape)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray.shape)
blur = cv2.GaussianBlur(gray, (5, 5),
                       cv2.BORDER_DEFAULT)
# retval, dst = cv.threshold( src, thresh, maxval, type[, dst] ) 

ret, thresh = cv2.threshold(blur, 255 * 0.85, 255,
                           cv2.THRESH_BINARY_INV)
print(thresh)
contours, hierarchies = cv2.findContours( 
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
# blank = np.zeros(thresh.shape[:2],
#                  dtype='uint8')
# print("==============")

# print(blank)
# cv2.drawContours(blank, contours, -1,
#                 (255, 0, 0), 1)
 
# cv2.imwrite("Contours.png", blank)
center_points = []

# center points we will be using the moments() 
for i in contours:
    # a list of 3D numpy arrays where each is of size N x 1 x 2 
    # where N is the total number of contour points for each object.
    print(i.shape)
    M = cv2.moments(i)
    area = cv2.contourArea(i[0])
    if M['m00'] != 0 and M['m00'] >= 250:
        # 空间矩
        # print("area "+str(M['m00']))
        # perimeter = cv2.arcLength(i,True)
        # print("perimeter " + str(perimeter))
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        center_points.append([cx,cy])
        cv2.drawContours(image, [i], -1, (0, 255, 0), 2)
        mask = np.zeros(image.shape[:2],dtype='uint8')
        # mask = np.zeros(image.shape)
        mean,stddev = cv2.meanStdDev(image,mask=mask)
        print("mean: " + str(mean))
        cv2.circle(image, (cx, cy), 4, (255, 0, 0), -1) 
        # cv2.putText(image, "center", (cx - 20, cy - 20),
        #            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    # print(f"x: {cx} y: {cy}")
print("center_points number: " + str(len(center_points)))
print(center_points)
visited = np.zeros(len(center_points))
print(visited)
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





# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# buildPointsGroup(center_points, visited)
# print(all_group_points)
# print(len(all_group_points))

# light_orange = (1, 190, 200)
# red = (255, 0, 0)
# pink = (255, 153, 255)
# colors = []
# colors.append(red)
# colors.append(light_orange)
# colors.append(pink)   








# def printPixelValWithThresh(src, threshold):
#     rows,cols = src.shape #rows is y in imageJ
#     for i in range(rows):
#         for j in range(cols):
#             k = src[i,j]
#             # if j == 519 and i == 207:
#             #     print(k) 
#             #     break
#             if k > threshold:
#                 print("X: " + str(j) + " Y: " + str(i) + " Value: " + str(k))


# # cv2.circle(image, (cx, cy), 4, (255, 0, 0), -1) 

# fig,ax = plt.subplots(1)
# ax.imshow(image)
# plt.show()
# # cv2.imshow('image', image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

