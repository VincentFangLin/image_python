from PlateImageProcess import PlateImageProcess
from PositionImageProcess import PositionImageProcess
from constants.PositionFolderName import PositionFolderName
from constants.PositionImageName import PositionImageName
import matplotlib.pyplot as plt
from CombinePositionImages import CombinePositionImages
from ShowImages import ShowImages



class FetchPositionImageData:
    def __init__(self,position_folder_path):
        self.position_folder_path = position_folder_path
    def get_position_image_path(self):
        position_paths = []
        for i in range(0,len(PositionFolderName.NAME)):
            pfn = PositionFolderName.NAME
            pin = PositionImageName.NAME
            position_image_path = self.position_folder_path + str(pfn[i]) + '/' + str(pin[i]) + '.tif'
            position_paths.append(position_image_path)
        return position_paths
    def convert_index(self,index):#index to coord
        r = int(index / 12)
        c = index % 12
        coord = str(chr(r + ord('A')))+str(c + 1)
        return coord
    def get_postion_image_info(self,position_paths):
        chip_coord_and_ROI_idx_dic = {}
        for i in range(0,len(position_paths)):
            coord = self.convert_index(i)
            print("========================== " + str(coord) + " ==========================")
            Position_IP = PositionImageProcess(position_paths[i])
            ROI_chip_idx,missing_chip_centers = Position_IP.position_image_process(coord)#start from 1
            chip_coord_and_ROI_idx_dic[coord] = ROI_chip_idx
        return chip_coord_and_ROI_idx_dic

