from PlateImageProcessing import PlateImageProcessing
from PositionImageProcessing import PositionImageProcessing
import cv2
import matplotlib.pyplot as plt
import math



def plate_image_process(image_path):
    IP = PlateImageProcessing(image_path)

    thresh,plate_image,drew_image = IP.image_preprocessing()

    contours_center_points = IP.find_and_drew_contours(drew_image, thresh)

    all_group_points = IP.build_points_group(contours_center_points)

    group_with_four_or_three_points = IP.filter_group_points(all_group_points)

    group_centers = IP.get_group_center(group_with_four_or_three_points)
        
    corners, positive_slope = IP.find_corners(drew_image,group_centers)

    theta = IP.get_theta(group_with_four_or_three_points)

    pillar_name_and_coord_dic = IP.get_pillar_name_and_coord_dic(drew_image,group_centers,corners,theta,positive_slope)

    print(pillar_name_and_coord_dic)


    IP.draw_chip_position(drew_image, pillar_name_and_coord_dic,positive_slope,theta)

    position_and_data_Dic = IP.get_plate_img_data(plate_image,pillar_name_and_coord_dic,12,math.degrees(theta), True)
    # print(position_and_data_Dic)


def position_image_process(image_path):
    IP = PositionImageProcessing(image_path)
    image,contours = IP.getROI()
    centerPoints = IP.getCenterPointsOfROI(image, contours)
    ROI_chip_idx_and_center,fourCornersDic,missing_chip_centers = IP.drawCenterPoints(image,centerPoints)
    # print("fourCornersDic " + str(fourCornersDic))
    print("missingCenterPoints " + str(missing_chip_centers))
    ROI_chip_idx = list(ROI_chip_idx_and_center.keys())
    print("ROI: " + str(ROI_chip_idx))

    return ROI_chip_idx,missing_chip_centers








position_and_data_Dic = plate_image_process("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif")
print('========================================================================================================')
ROI_chip_idx_and_center,missing_chip_centers = position_image_process("C:/Users/Vibrant/Desktop/openCV/positions/image0.tif")