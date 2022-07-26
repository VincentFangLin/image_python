import matplotlib.pyplot as plt
import cv2
image = cv2.imread("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif",cv2.IMREAD_ANYDEPTH)

plt.ion()    # 打开交互模式
# 同时打开两个窗口显示图片
plt.figure()  #图片一
plt.imshow(image)

print("=========================================")
print(1+2)
print("dagregaerg")
# plt.figure()    #图片二
# plt.imshow(image)
# 显示前关掉交互模式
plt.ioff()#plt.show()之前一定不要忘了加plt.ioff()，如果不加，界面会一闪而过，并不会停留
plt.show()
