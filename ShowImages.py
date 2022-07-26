import matplotlib.pyplot as plt
import cv2

class ShowImages:
    def show_images(image1,image2):
        fig,(ax1,ax2) = plt.subplots(1, 2)
        ax1.imshow(image1)
        ax2.imshow(image2)
        plt.show()
    def show_image(image):
        fig,ax = plt.subplots(1)
        ax.imshow(image)
        plt.show()
    def show_images_two_windows(image1,image2):
        fig,ax1 = plt.subplots(1)
        ax1.imshow(image1)
        fig,ax2 = plt.subplots(1)
        ax2.imshow(image1)
        ax2.imshow(image2)
        plt.show()
    def show_real_image(image_path):
        image = cv2.imread(image_path,cv2.IMREAD_ANYDEPTH)
        fig,ax = plt.subplots(1)
        ax.imshow(image)
        plt.show()