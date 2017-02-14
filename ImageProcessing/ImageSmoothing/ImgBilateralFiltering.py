import cv2
import numpy as np

img = cv2.imread('wood.jpg')

ImgBilateralFiltered = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('wood.jpg', img)
cv2.imshow('ImgBilateralFiltered', ImgBilateralFiltered)
cv2.waitKey(0)
cv2.destroyAllWindows()