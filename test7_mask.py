import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img1.tif", cv2.IMREAD_COLOR)
print("image shape: " + str(image.shape))
msk = np.zeros(image.shape, np.uint8)
print("msk shape: " +  str(msk.shape))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("gray shape: " +  str(gray.shape))

# cv2.bilateralFilter(image, 5, 200, 5)
# im2 = cv2.GaussianBlur(image,(5,5),0)
blur = cv2.GaussianBlur(gray, (5, 5),
                       cv2.BORDER_DEFAULT)
# retval, dst = cv.threshold( src, thresh, maxval, type[, dst] ) 

ret, thresh = cv2.threshold(blur, 255 * 0.85, 255,
                           cv2.THRESH_BINARY_INV)
contours, heir = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# 第一个参数是指明在哪幅图像上绘制轮廓；image为三通道才能显示轮廓
# 第二个参数是轮廓本身，在Python中是一个list
# 第三个参数指定绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓
cv2.drawContours(msk, contours, -1, 255, 5)
print(msk)
# print (cv2.mean(thresh , mask = msk))

print("number of contours: " + str(len(contours)))
# res = np.zeros(image.shape, np.uint8)
# print(res.shape)
count = 0
for cnt in contours:
    if count == 0:
        count = count + 1
        continue
    # print(cnt)
    res = np.zeros(image.shape[:2], np.uint8)
    # print("res shape: " +  str(res.shape))
    # center - 圆心  (x, y)  radius - 半径  r
    (x,y), radius = cv2.minEnclosingCircle(cnt) 
    ctr = (int(x), int(y))
    rad = int(radius)
    # cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
    print("ctr " + str(ctr))
    print("rad " + str(rad))
    circ = cv2.circle(res, ctr, rad,255,5)
    print("===============")
    print(res.shape)
    # cv2.drawContours(msk, contours, -1, 255, -1)
    print ("Area: " + str(cv2.contourArea(cnt)), "Mean: " + str(float(cv2.meanStdDev(thresh, mask=res)[0])))
    count = count + 1

# fig,ax = plt.subplots(1)
# ax.imshow(res)
# plt.show()
# # cv2.imshow('image', image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

