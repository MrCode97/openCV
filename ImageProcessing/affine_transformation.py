import cv2
import numpy as np

img = cv2.imread('squares.jpg')
rows,cols,ch = img.shape

# 1. You define 3 points (on the picture [=img]) -> it gets the (vector-)plane [geometry] of them. 
pointsN = np.float32(([50,50],[200,50],[50,200]))
# 2. You set the (transformed-)points where the points from above (1.) shall be afterwards. 
#   So that it later can calc the new (transformed-)plane [=tranfromation].
pointsT = np.float32(([10,100],[200,50],[100,250]))

# gets openCV solved the matrix, so that the plane translates that pointN -> pointT 
matrixTransform = cv2.getAffineTransform(pointsN, pointsT)

# tranform-act
transformedImg = cv2.warpAffine(img, matrixTransform, (cols, rows))

# This is only for a better understanding: shows you the point we used for the m1.atrix. 
# You'll see that this point are not drawn on the img and the transformed! 
# But you'll note that those are the same points on the picture[chess1.jpg] but not on the img.
#
# see (1.) 
cv2.circle(img, (50, 50), 10, (0, 0, 255), -1)                  # pointsN (1) - red
cv2.circle(img, (200, 50), 10, (0, 0, 255), -1)                 # pointsN (2) - red
cv2.circle(img, (50, 200), 10, (0, 0, 255), -1)                 # pointsN (3) - red
# see (2.)
cv2.circle(transformedImg, (10, 100), 10, (0, 255, 255), -1)    # pointsT (1) - yellow
cv2.circle(transformedImg, (200, 50), 10, (0, 255, 255), -1)    # pointsT (2) - yellow
cv2.circle(transformedImg, (100, 250), 10, (0, 255, 255), -1)   # pointsT (3) - yellow
#

# display Imgs
cv2.imshow('original', img)
cv2.imshow('transformed', transformedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
