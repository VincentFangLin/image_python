import matplotlib.pyplot as plt
import cv2


# for pn in PositionName.NAME:
#     print(pn)


# def convert_index(index):
#     r = int(index / 12)
#     c = index % 12
#     coord = str(chr(r + ord('A')))+str(c + 1)
#     print(coord)

# convert_index(95)
# for i in range(0, 96):
#     r = int(i / 12)
#     c = i % 12
#     coord = str(chr(r + ord('A')))+str(c + 1)
#     print(coord)
image1 = cv2.imread("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif", cv2.IMREAD_COLOR)
image2 = cv2.imread("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif", cv2.IMREAD_COLOR)


fig,(ax1,ax2) = plt.subplots(1, 2)
ax1.imshow(image1)
ax2.imshow(image2)

plt.show()

