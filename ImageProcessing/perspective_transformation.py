import cv2
import numpy as np

# load img
img = cv2.imread('text.jpg')

# set points (before -> afterwards)
pointsN = np.float32([[464, 342], [1620, 556], [379, 1117], [1608, 1275]])
pointsT = np.float32([[0, 0], [900, 0], [0, 600], [900, 600]])

# get matrix & apply
matrix = cv2.getPerspectiveTransform(pointsN, pointsT)
transformedImg = cv2.warpPerspective(img, matrix, (900, 600))

# show and destroy
cv2.imshow('transformed-Img', transformedImg)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()