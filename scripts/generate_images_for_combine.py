import matplotlib.pyplot as plt
import math
import numpy as np
import cv2

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
for i in range(2,97):
    image = mpimg.imread("processed_position_images/combined_image_1.jpeg")
    # fig,ax = plt.subplots(1)
    # ax.imshow(image)
    # plt.show()
    plt.imsave('processed_position_images/' + 'combined_image_' + str(i) +'.jpeg', image)


