import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.zeros((270,474, 3), dtype = "uint8")
print(img.shape)
green = (0, 255, 0)
cv2.line(img, (0, 0), (474, 270), green)

red = (255, 0, 0)
R = 100
(centerX, centerY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.circle(img, (centerX, centerY), R , red)

plt.imshow(img)
plt.show()