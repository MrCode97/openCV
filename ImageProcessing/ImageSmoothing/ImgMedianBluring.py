import cv2
import numpy as np

# load Img
img = cv2.imread('original.png')

# create new medianBlured Img
ImgMedianBlur = cv2.medianBlur(img, 5)  # 5 is kernel size (the higher the more BLUR)

# show and close 
cv2.imshow('original.jpg', img)
cv2.imshow('ImgMedianBlured', ImgMedianBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()