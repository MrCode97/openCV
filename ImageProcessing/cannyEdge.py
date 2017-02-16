import cv2
import numpy as np

img = cv2.imread('original.jpg', 0)

# Apply CannyEdge: give min and max Threshold-Value
edges = cv2.Canny(img, 100, 300)    # cv2.Canny(source, param threshold1, param threshold2) -> thr1 (=min), thr2 (=max)

cv2.imshow('original', img)
cv2.imshow('edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindow()