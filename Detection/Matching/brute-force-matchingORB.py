import cv2
import numpy as np

searchImg = cv2.imread('cover.jpg', 0)          # Picture that we are looking for
container = cv2.imread('cont1.jpg', 0)          # Picture which contains the picture we are looking for

# Initiate ORB detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with ORB
keyPoints_search, des_search = orb.detectAndCompute(searchImg, None)
keyPoints_container, des_container = orb.detectAndCompute(container, None)

# create BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)   # crossCheck=false (default); crossCheck=True -> better result

# Match descriptors.
matches = bf.match(des_search, des_container)

# Sort them in the order of their distance.
# We sort them in ascending order of their distances so that best matches (with low distance) come to front.
matches = sorted(matches, key = lambda x:x.distance)

# Draw only first 10 matches (because of visibility)
result = cv2.drawMatches(searchImg, keyPoints_search, container, keyPoints_container, matches[:10], None, flags=2)  # Note although it says that 'outImg' is optional I had to fill it with 'None'
# similar to cv2.drawKeypoints but cv2.drawMatches draws the matches: puts two picture side by side and draws lines for one to the other (matches)
# (There is also cv2.drawMatchesKnn which draws all the k best matches.)

cv2.imwrite('bf-matchORB.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
