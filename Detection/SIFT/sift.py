import cv2
import numpy as np

skyline = cv2.imread('skyline.jpg')
skylineGRAY = cv2.imread('skyline.jpg', 0)

# create sift object
sift = cv2.xfeatures2d.SIFT_create()

# get / detect KeyPoints on 'skylineGRAY'
keyPoints = sift.detect(skylineGRAY, None)
# sift.detect() function finds the keypoint in the images. You can pass a mask if you want to search only a part of image.
# Each keypoint is a special structure which has many attributes like its (x,y) coordinates, size of the meaningful neighbourhood,
# angle which specifies its orientation, response that specifies strength of keypoints etc.
# src: docs.opencv.org/

# create new img where the keyPoints are drawn on the coloredSkyline
skylineKeyPoints = cv2.drawKeypoints(skyline, keyPoints, skylineGRAY)

# adds the size and th e orientation of the KeyPoints
skylineKeyPointsSizeOrientation = cv2.drawKeypoints(skyline, keyPoints, skylineGRAY, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('sift_keypoints.jpg',skylineKeyPointsSizeOrientation)
cv2.imwrite('skylineKeyPointsSizeOrientation.jpg', skylineKeyPointsSizeOrientation)

cv2.imshow('Skyline with KeyPoints', skylineKeyPoints)
cv2.imwrite('SkylineKeyPoints.jpg', skylineKeyPoints)

cv2.waitKey(0)
cv2.destroyAllWindows()
