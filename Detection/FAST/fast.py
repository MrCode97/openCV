import cv2
import numpy as np

img = cv2.imread('robot.png', 0)

# create FAST object
fast = cv2.FastFeatureDetector_create()

# FAST with nonmaxSuppression
#
# get keyPointsT (nonmaxSuppression=True)
keyPointsT = fast.detect(img, None)
# draw keyPointsT on new object: fastTrue
fastTrue = cv2.drawKeypoints(img, keyPointsT, None, (255, 0, 0))        # blue
cv2.imwrite('fast_robot_nonmaxSuppression_TRUE.jpg', fastTrue)
cv2.imshow('FAST: with nonmaxSuppression', fastTrue)

# show default params
print "Threshold: ", fast.getThreshold()
print "nonmaxSuppression: ", fast.getNonmaxSuppression()
print "neighborhood: ", fast.getType()
print "Total Keypoints with nonmaxSuppression: ", len(keyPointsT)


# FAST without nonmaxSuppression
#
# set nonmaxSuppression to false
fast.setNonmaxSuppression(0)
# get keyPointsT (nonmaxSuppression=False)
keyPointsF = fast.detect(img, None)
# draw keyPointsT on new object: fastTrue
fastFalse = cv2.drawKeypoints(img, keyPointsF, None, (0, 0, 255))       # red
cv2.imwrite('fast_robot_nonmaxSuppression_FALSE.jpg', fastFalse)
cv2.imshow('FAST: without nonmaxSuppression', fastFalse)

print "Total Keypoints without nonmaxSuppression: ", len(keyPointsF)

cv2.waitKey(0)
cv2.destroyAllWindows()
