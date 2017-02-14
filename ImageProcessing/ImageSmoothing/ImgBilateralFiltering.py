import cv2
import numpy as np

# load img
img = cv2.imread('wood.jpg')

# create new bilateralfiltered picture from original ('img')
ImgBilateralFiltered = cv2.bilateralFilter(img, 9, 75, 75)      # 9 -> param d
                                                                # 75 -> sigmaColor
                                                                # 75 -> sigmaSpace
# show imgs and close 
cv2.imshow('wood.jpg', img)
cv2.imshow('ImgBilateralFiltered', ImgBilateralFiltered)
cv2.waitKey(0)
cv2.destroyAllWindows()