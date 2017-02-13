import cv2
import numpy as np

img = cv2.imread('original.jpg')

ImgBLUR = cv2.blur(img, (5, 5))

cv2.imshow('ImgBlured', ImgBLUR)
cv2.waitKey(0)
cv2.destroyAllWindows()