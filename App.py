from PlateImageProcess import PlateImageProcess
from PositionImageProcess import PositionImageProcess
from constants.PositionFolderName import PositionFolderName
from constants.PositionImageName import PositionImageName
import matplotlib.pyplot as plt
from CombinePositionImages import CombinePositionImages

def get_position_image_path(position_folder_path):
    position_paths = []
    for i in range(0,len(PositionFolderName.NAME)):
        pfn = PositionFolderName.NAME
        pin = PositionImageName.NAME
        position_image_path = position_folder_path + str(pfn[i]) + '/' + str(pin[i]) + '.tif'
        position_paths.append(position_image_path)
    return position_paths
def convert_index(index):#index to coord
    r = int(index / 12)
    c = index % 12
    coord = str(chr(r + ord('A')))+str(c + 1)
    return coord
def get_postion_image_info(position_paths):
    chip_coord_and_ROI_idx_dic = {}
    for i in range(0,len(position_paths)):
        coord = convert_index(i)
        print("========================== " + str(coord) + " ==========================")
        Position_IP = PositionImageProcess(position_paths[i])
        ROI_chip_idx,missing_chip_centers = Position_IP.position_image_process(coord)#start from 1
        chip_coord_and_ROI_idx_dic[coord] = ROI_chip_idx
    return chip_coord_and_ROI_idx_dic
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
position_folder_path = get_position_image_path("C:/Users/Vibrant/Desktop/Scanned Plate/CVTG80010001000072/TileScan 1/")
chip_coord_and_ROI_idx_dic = get_postion_image_info(position_folder_path)

Plate_IP = PlateImageProcess("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif",chip_coord_and_ROI_idx_dic)
position_and_data_Dic,draw_plate_image = Plate_IP.plate_image_process()
print(position_and_data_Dic)

# cpi = CombinePositionImages()
# combined_image = cpi.getCombinedImage()
# draw_combined_image = cpi.drawIndex(combined_image)
show_image(draw_plate_image)
# show_images_two_windows(draw_combined_image,draw_plate_image)
# show_images(draw_combined_image,draw_plate_image)