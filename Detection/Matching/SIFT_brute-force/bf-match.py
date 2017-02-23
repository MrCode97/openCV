import numpy as np
import cv2

searchImg = cv2.imread('cv.jpg', 0)        # Picture that we are looking for
container = cv2.imread('cont2.jpg', 0)          # Picture which contains the picture we are looking for
# create SIFT
sift = cv2.xfeatures2d.SIFT_create()

# get keypoints, descriptors with SIFT
keyPoints_search, des_search = sift.detectAndCompute(searchImg, None)
keyPoints_container, des_container = sift.detectAndCompute(container, None)

# create BFMatcher (default params)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des_search,des_container, k=2)

# ratio test
good = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
result = cv2.drawMatchesKnn(searchImg, keyPoints_search, container, keyPoints_container, good, None, flags=2) # Note although it says that 'outImg' is optional I had to fill it with 'None'

cv2.imwrite('bf-matchSIFT-picTxt.jpg', result)
