import cv2
import numpy as np

# load img
img = cv2.imread('text.jpg')

# set points (before -> afterwards) see below (pointsN, pointsT)
pointsN = np.float32([[464, 342], [1620, 556], [379, 1117], [1608, 1275]])
pointsT = np.float32([[0, 0], [900, 0], [0, 600], [900, 600]])

# get matrix (solved)
matrix = cv2.getPerspectiveTransform(pointsN, pointsT)
# apply transformation on new 'transformedImg'
transformedImg = cv2.warpPerspective(img, matrix, (900, 600))


# This is only for a better understanding and absolutly not necessary:
#
# pointsN:
# With those points (pointsN) you define the area (on the original picture) which shall be "cut" and transformed.
# Note that the points are in the following order:                  # p' (x, y)         location        colored
#
cv2.circle(img, (464, 342), 10, (255, 255, 255), -1)                # p1 (464, 342)     TopLeft         white
cv2.circle(img, (1620, 556), 10, (0, 255, 255), -1)                 # p2 (1620, 556)    TopRight        yellow
cv2.circle(img, (379, 1117), 10, (0, 165, 255), -1)                 # p3 (379, 1117)    BottomLeft      orange
cv2.circle(img, (1608, 1275), 10, (0, 0, 255), -1)                  # p4 (1608, 1275)   BottomRight     red
#
# pointsT:
# Here you define now where those pointsN now shall appear (transformed).
# In the same order as on above (TopLeft, TopRight, BottomLeft, BottomRight)
# Make sure the points (x|y) are in the range of the new-generated img: => [cv2.warpPerspective(.., (*900, 600*))] -> line 13
cv2.circle(transformedImg, (0, 0), 10, (255, 255, 255), -1)         # p1 (0, 0)         TopLeft         white
cv2.circle(transformedImg, (900, 0), 10, (0, 255, 255), -1)         # p2 (900, 0)       TopRight        yellow
cv2.circle(transformedImg, (0, 600), 10, (0, 165, 255), -1)         # p3 (0, 600)       BottomLeft      orange
cv2.circle(transformedImg, (900, 600), 10, (0, 0, 255), -1)         # p4 (900, 600)     BottomRight     red
#
#

# show and destroy
cv2.imshow('transformed-Img', transformedImg)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()