import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("C:/Users/Vibrant/Desktop/openCV/positions/A1 Position1_ch00.tif")
img2 = cv2.imread("C:/Users/Vibrant/Desktop/openCV/positions/A2 Position1_ch00.tif")
img3 = cv2.imread("C:/Users/Vibrant/Desktop/openCV/positions/A3 Position1_ch00.tif")
img4 = cv2.imread("C:/Users/Vibrant/Desktop/openCV/positions/A4 Position1_ch00.tif")

img1 = cv2.resize(img1, None, fx=0.05, fy=0.05)    #为了完整显示，缩小一倍
# img2 = cv2.resize(img2, None, fx=0.05, fy=0.05)    #为了完整显示，缩小一倍
# img3 = cv2.resize(img3, None, fx=0.05, fy=0.05)    #为了完整显示，缩小一倍
# img4 = cv2.resize(img4, None, fx=0.05, fy=0.05)    #为了完整显示，缩小一倍



# # blur2 = cv2.blur(img, (2,2))
# # blur3 = cv2.blur(img, (5,5))
# # blur4 = cv2.blur(img, (10,10))

# htich = np.hstack((img1,img2))
# htich2 = np.hstack((img3,img4))
# vtich = np.vstack((htich, htich2))

# cv2.imshow("merged_img", img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

fig,ax = plt.subplots(1)
ax.imshow(img1)
plt.show()