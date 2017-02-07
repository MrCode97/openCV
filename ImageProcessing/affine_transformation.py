import cv2
import numpy as np

img = cv2.imread('squares.jpg')
rows,cols,ch = img.shape

# giving points -> translation
pointsN = np.float32(([50,50],[200,50],[50,200]))
pointsT = np.float32(([10,100],[200,50],[100,250]))

# get matrix from openCV
matrixTransform = cv2.getAffineTransform(pointsN, pointsT)

# tranform-act
transformedImg = cv2.warpAffine(img, matrixTransform, (cols, rows))

# This is only for a better understanding: shows you the point we used for the matrix. 
# You'll see that this point are not drawn on the img and the transformed! 
# But you'll note that those are the same points on the picture[chess1.jpg] but not on the img.
#
# pointsN
cv2.circle(img, (50, 50), 10, (0, 0, 255), -1)
cv2.circle(img, (200, 50), 10, (0, 0, 255), -1)
cv2.circle(img, (50, 200), 10, (0, 0, 255), -1)

# pointsT
cv2.circle(transformedImg, (10, 100), 10, (0, 255, 255), -1)
cv2.circle(transformedImg, (200, 50), 10, (0, 255, 255), -1)
cv2.circle(transformedImg, (100, 250), 10, (0, 255, 255), -1)


# display Imgs
cv2.imshow('original', img)
cv2.imshow('transformed', transformedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
