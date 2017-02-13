import cv2
import numpy as np

img = cv2.imread('original.jpg')

ImgMedianBlur = cv2.medianBlur(img, 5)

cv2.imshow('ImgMedianBlured', ImgMedianBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()