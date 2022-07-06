import cv2
import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image as im

# src = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img1.tif",cv2.IMREAD_ANYDEPTH)
# print(type(src))
# edges = cv2.Canny(src,100,200)

# plt.subplot(121),plt.imshow(src,cmap = 'gray')

# plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# plt.subplot(122),plt.imshow(edges,cmap = 'gray')

# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# print("============================")
# plt.show()

# define a main function
def main():
  
    # create a numpy array from scratch
    # using arange function.
    # 1024x720 = 737280 is the amount 
    # of pixels.
    # np.uint8 is a data type containing
    # numbers ranging from 0 to 255 
    # and no non-negative integers
    array = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img1.tif",cv2.IMREAD_ANYDEPTH)

      
    # check type of array
    print(type(array))
      
    # our array will be of width 
    # 737280 pixels That means it 
    # will be a long dark line
    print(array.shape)
      
    # Reshape the array into a 
    # familiar resoluition
    # array = np.reshape(array, (1024, 720))
      
    # show the shape of the array
    print(array.shape)
  
    # show the array
    print(array)
      
    # creating image object of
    # above array
    data = im.fromarray(array)
      # cv2.imshow('image',contours)
    cv2.circle(data, (500,500), radius=5, color=(0, 0, 255), thickness=-1)

    # saving the final output 
    # as a PNG file
    data.save('gfg_dummy_pic.png')
  
# driver code
if __name__ == "__main__":
    
  # function call
  main()