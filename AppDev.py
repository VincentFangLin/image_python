from ImageProcessing import ImageProcessing

IP = ImageProcessing("C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif")

thresh,plate_image,drew_image = IP.image_preprocessing()

contours_center_points = IP.find_and_drew_contours(drew_image, thresh)
print("contours_center_points: " + str(len(contours_center_points)))

all_group_points = IP.build_points_group(contours_center_points)

group_with_four_or_three_points = IP.filterGroupPoints(all_group_points)
