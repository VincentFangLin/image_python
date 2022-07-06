import cv2
import numpy as np

img = cv2.imread("C:/Users/Vibrant/Desktop/openCV/img1.tif",cv2.IMREAD_COLOR)
# img = np.array(img,dtype=np.uint32)
# print(img)
def printPixelValWithThresh(src, threshold):
    rows,cols = src.shape #rows is y in imageJ
    for i in range(rows):
        for j in range(cols):
            k = src[i,j]
            # if j == 519 and i == 207:
            #     print(k) 
            #     break
            if k > threshold :
                print("X: " + str(j) + " Y: " + str(i) + " Value: " + str(k))




# printPixelValWithThresh(img, 65535 * 0.9)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(gray.shape)
# blur = cv2.GaussianBlur(gray, (5, 5),
#                        cv2.BORDER_DEFAULT)
# # retval, dst = cv.threshold( src, thresh, maxval, type[, dst] ) 

# ret, thresh = cv2.threshold(blur, 255 * 0.85, 255,
#                            cv2.THRESH_BINARY_INV)
# print(thresh)
contours, hierarchies = cv2.findContours( 
    img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
# blank = np.zeros(img.shape[:2],
#                  dtype='uint8')
# print(blank)
# cv2.imshow('test', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
