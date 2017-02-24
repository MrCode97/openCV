import numpy as np
import cv2

# Pictures are in ./res
searchImg = cv2.imread('cover.jpg', 0)          # Picture that we are looking for
container = cv2.imread('cont1.jpg', 0)          # Picture which contains the picture we are looking for

# create SIFT
sift = cv2.xfeatures2d.SIFT_create()       # cv2.SIFT() doesn't work in my env (openCV: 3.1.0)

# get keypoints, descriptors with SIFT
keyPoints_search, des_search = sift.detectAndCompute(searchImg, None)
keyPoints_container, des_container = sift.detectAndCompute(container, None)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des_search, des_container, k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0, 0] for i in xrange(len(matches))]

# ratio test (like in Lowe's paper)
for i, (m, n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1, 0]

draw_params = dict(matchColor = (0, 255, 0),
                   singlePointColor = (255, 0, 0),
                   matchesMask = matchesMask,
                   flags = 0)

img3 = cv2.drawMatchesKnn(searchImg, keyPoints_search, container, keyPoints_container, matches, None, **draw_params)
cv2.imwrite('test.jpg', img3)
