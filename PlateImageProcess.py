from image_process_functions.PlateImageProcessing import PlateImageProcessing
from image_process_functions.PositionImageProcessing import PositionImageProcessing
import cv2
import matplotlib.pyplot as plt
import math
import numpy as np
from constants.PositionFolderName import PositionFolderName

class PlateImageProcess:
    def __init__(self, image_path):
        self.image_path = image_path

    def plate_image_process(self):
        IP = PlateImageProcessing(self.image_path)

        thresh,plate_image,drew_image = IP.image_preprocessing()

        contours_center_points = IP.find_and_drew_contours(drew_image, thresh)

        all_group_points = IP.build_points_group(contours_center_points)

        group_with_four_or_three_points = IP.filter_group_points(all_group_points)

        group_centers = IP.get_group_center(group_with_four_or_three_points)
            
        corners, positive_slope = IP.find_corners(drew_image,group_centers)

        theta = IP.get_theta(group_with_four_or_three_points)

        pillar_name_and_coord_dic = IP.get_pillar_name_and_coord_dic(drew_image,group_centers,corners,theta,positive_slope)
        

        IP.draw_chip_position(drew_image, pillar_name_and_coord_dic,positive_slope,theta)

        position_and_data_Dic = IP.get_plate_img_data(plate_image,pillar_name_and_coord_dic,12,math.degrees(theta), True)

        # # print(position_and_data_Dic)
        # fig,ax = plt.subplots(1)
        # ax.imshow(drew_image)
        # plt.show()
        return position_and_data_Dic,drew_image


# Plate_IP = PlateImageProcess("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif")
# position_and_data_Dic = Plate_IP.plate_image_process()
