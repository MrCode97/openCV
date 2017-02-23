import numpy as np
import cv2

searchImg = cv2.imread('cover.jpg', 0)          # queryImage
container = cv2.imread('cont1.jpg', 0) # trainImage

# create SIFT
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
keyPoints_search, des_search = sift.detectAndCompute(searchImg, None)
keyPoints_container, des_container = sift.detectAndCompute(container, None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des_search,des_container, k=2)

# Apply ratio test
good = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(searchImg, keyPoints_search, container, keyPoints_container, good, None, flags=2)

cv2.imwrite('SIFT-matching.jpg', img3)
