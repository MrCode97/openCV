import numpy as np
import cv2

eagle = cv2.imread('eagle.jpg', 0)
skyline = cv2.imread('skyline.jpg', 0)

# create ORB detector
orb = cv2.ORB_create()

# detect keypoints with ORB
keyPointsEagle = orb.detect(eagle, None)
keyPointsSkyline = orb.detect(skyline, None)

# compute the descriptors with ORB
keyPointsEagle, des_Eagle = orb.compute(eagle, keyPointsEagle)
keyPointsSkyline, des_Skyline = orb.compute(skyline, keyPointsSkyline)

# draw keypoints location -not size and orientation
ORB_Eagle = cv2.drawKeypoints(eagle, keyPointsEagle, None, (0, 255, 0))         # draw green
ORB_Skyline = cv2.drawKeypoints(skyline, keyPointsSkyline, None, (0, 255, 0))   # ""

# display and write
cv2.imshow('ORB_Eagle', ORB_Eagle)
cv2.imshow('ORB_Skyline', ORB_Skyline)
cv2.imwrite('ORB_Eagle.jpg', ORB_Eagle)
cv2.imwrite('ORB_Skyline.jpg', ORB_Skyline)
cv2.waitKey(0)
cv2.destroyAllWindows()
