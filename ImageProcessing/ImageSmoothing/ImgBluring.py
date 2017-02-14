import cv2
import numpy as np

# load Img
img = cv2.imread('original.png')

# create new blured Img
ImgBLUR = cv2.blur(img, (5, 5))     # (5, 5) == kernel size

# show and close
cv2.imshow('original.png', img)
cv2.imshow('ImgBlured', ImgBLUR)
cv2.waitKey(0)
cv2.destroyAllWindows()