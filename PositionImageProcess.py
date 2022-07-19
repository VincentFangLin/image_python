from image_process_functions.PositionImageProcessing import PositionImageProcessing
import matplotlib.pyplot as plt
from constants.PositionFolderName import PositionFolderName

class PositionImageProcess:
    def __init__(self, image_path):
        self.image_path = image_path

    def position_image_process(self, idx):
        IP = PositionImageProcessing(self.image_path)
        image,contours = IP.getROI()
        centerPoints = IP.getCenterPointsOfROI(image, contours)
        ROI_chip_idx_and_center,fourCornersDic,missing_chip_centers = IP.drawCenterPoints(image,centerPoints)
        # print("fourCornersDic " + str(fourCornersDic))
        print("missingCenterPoints " + str(missing_chip_centers))
        ROI_chip_idx = list(ROI_chip_idx_and_center.keys())
        print("ROI: " + str(ROI_chip_idx))
        IP.drawCenterPoints(image,centerPoints)
        plt.imsave('processed_position_images/combined_image' + '_' + str(idx) + '.jpeg', image)
        # IP.showImage(image)
        return ROI_chip_idx,missing_chip_centers



# Position_IP = PositionImageProcess("C:/Users/Vibrant/Desktop/openCV/A1 Position1/A1 Position1_ch00.tif")
# position_and_data_Dic = Position_IP.position_image_process()