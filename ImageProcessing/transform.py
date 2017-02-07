import cv2
import numpy as np
img = cv2.imread('chess1.jpg')

# resize-way1
way1 = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

# resize-way2
height, width = img.shape[:2]
way2 = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)


# display and destroy
cv2.imshow('original', img)
cv2.imshow('way1', way1)
cv2.imshow('way2', way2)
cv2.waitKey(0)
cv2.destroyAllWindows()