from PlateImageProcess import PlateImageProcess
from PositionImageProcess import PositionImageProcess
from constants.PositionFolderName import PositionFolderName
from constants.PositionImageName import PositionImageName
import matplotlib.pyplot as plt
from CombinePositionImages import CombinePositionImages
from ShowImages import ShowImages
from FetchPositionImageData import FetchPositionImageData


class ImageProcessApp:
    def __init__(self,position_folder_path,plate_image_path):
        self.position_folder_path = position_folder_path
        self.plate_image_path = plate_image_path
    
    def run(self):
        fetchPositionImageData = FetchPositionImageData(self.position_folder_path)
        position_image_path =fetchPositionImageData.get_position_image_path()
        chip_coord_and_ROI_idx_dic = fetchPositionImageData.get_postion_image_info(position_image_path)

        Plate_IP = PlateImageProcess(self.plate_image_path,chip_coord_and_ROI_idx_dic)
        position_and_data_Dic,draw_plate_image = Plate_IP.plate_image_process()
        print(position_and_data_Dic)

        cpi = CombinePositionImages()
        combined_image = cpi.getCombinedImage()
        draw_combined_image = cpi.drawIndex(combined_image)
        # show_image(draw_plate_image)
        ShowImages.show_images_two_windows(draw_combined_image,draw_plate_image)
        # show_images(draw_combined_image,draw_plate_image)
        return position_and_data_Dic,chip_coord_and_ROI_idx_dic


# imageProcessApp = ImageProcessApp("C:/Users/Vibrant/Desktop/Scanned Plate/CVTG80010001000072/TileScan 1/","C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif")
# position_and_data_Dic = imageProcessApp.run()
# # print(position_and_data_Dic)
