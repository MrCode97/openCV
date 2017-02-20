import numpy as np
import cv2

img = cv2.imread('cube.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# get corner (x, y)
corners = cv2.goodFeaturesToTrack(gray, 5, 0.01, 10)    # ..(img, maxCorners, qualityLevel, minDistance)
corners = np.int0(corners)

# draw (red) points (where corners are) on Img
for i in corners:
    x,y = i.ravel()
    cv2.circle(img, (x,y), 3, (0, 0, 255), -1)

cv2.imwrite('Detection.jpg', img)
cv2.waitKey()
cv2.destroyAllWindows()