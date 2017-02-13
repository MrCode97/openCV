import cv2
import numpy as np

# By filtering an Image you loss sharpness but you get a smoother Img.

img = cv2.imread('ImgFiltering_original.jpg')

# Create kernel
kernel = np.ones((5, 5), np.float32)/25     # Here (5, 5) creats the size: 5x5 -> So thats kind of a "block" (X: 5-pixels; Y: 5-pixels)
                                            #                                     px1, px2, px3, px4, px5
                                            #                                     py2 
                                            #                                     py3
                                            #                                     py4
                                            #                                     py5
                                            # '/25' devided by 25 (=5x5) => creats new pixel value => brighter or darker
# Apply 
filteredImg = cv2.filter2D(img, -1, kernel)

# Show
cv2.imshow('original', img)
cv2.imshow('filtered', filteredImg)
cv2.waitKey(0)
cv2.destroyAllWindows()