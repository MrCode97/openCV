import cv2
import numpy as np

skyline = cv2.imread('skyline.jpg')
skylineGRAY = cv2.imread('skyline.jpg', 0)

# Option 1
#
# create sift object
sift = cv2.xfeatures2d.SIFT_create()
# get / detect KeyPoints on 'skylineGRAY'
keyPoints = sift.detect(skylineGRAY, None)
# computes descriptors from keypoint
ComputeKP1, des1 = sift.compute(skylineGRAY, keyPoints)   # ComputeKP gives us a list uf found keyPoints
# des is a numpy array of shape \(Number\_of\_Keypoints \times 128\)
# print des


# Option 2
#
sift2 = cv2.xfeatures2d.SIFT_create()
ComputeKP2, des2 = sift2.detectAndCompute(skylineGRAY, None)

cv2.waitKey(0)
cv2.destroyAllWindows()
