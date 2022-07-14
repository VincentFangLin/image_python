import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import segmentation
from datetime import datetime

import argparse
 
# import cv2
# # 导入必要的包
# import numpy as np
 
# # 构建命令行参数及解析
# # --image 输入图像路径
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", type=str, default="yc.jpg",
#                 help="path to the input image")
# args = vars(ap.parse_args())
 
# # 加载原始输入图像，并展示
# image = cv2.imread(args["image"])
# cv2.imshow("Original", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

 
# # # 掩码和原始图像具有相同的大小，但是只有俩种像素值：0（背景忽略）、255（前景保留）
# mask = np.zeros(image.shape[:2], dtype="uint8")
# cv2.rectangle(mask, (30, 90), (280, 440), 255, -1)
# cv2.imshow("Rectangular Mask", mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


print(datetime.now())