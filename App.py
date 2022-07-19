from PlateImageProcess import PlateImageProcess
from PositionImageProcess import PositionImageProcess
from constants.PositionFolderName import PositionFolderName
from constants.PositionImageName import PositionImageName






def get_position_image_path(position_folder_path):
    position_paths = []
    for i in range(0,len(PositionFolderName.NAME)):
        pfn = PositionFolderName.NAME
        pin = PositionImageName.NAME
        position_image_path = position_folder_path + str(pfn[i]) + '/' + str(pin[i]) + '.tif'
        position_paths.append(position_image_path)
    return position_paths

def get_postion_image_info(position_paths):
    for i in range(0,len(position_paths)):
        print("========================== " + str(i + 1) + " ==========================")
        # print(position_paths[i])
        Position_IP = PositionImageProcess(position_paths[i])
        Position_IP.position_image_process(i + 1)#start from 1





position_folder_path = get_position_image_path("C:/Users/Vibrant/Desktop/Scanned Plate/CVTG80010001000072/TileScan 1/")
get_postion_image_info(position_folder_path)
# print(position_paths)
# Position_IP = PositionImageProcess("C:/Users/Vibrant/Desktop/openCV/A1 Position1/A1 Position1_ch00.tif")
# position_and_data_Dic = Position_IP.position_image_process()
# Plate_IP = PlateImageProcess("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif")
# position_and_data_Dic = Plate_IP.plate_image_process()

