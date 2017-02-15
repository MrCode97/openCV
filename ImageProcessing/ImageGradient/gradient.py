import cv2
import numpy as np

# load img
img = cv2.imread('original.jpg',0)

# apply Laplacian function
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# apply Sobel function
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  # (1, 0) -> order of the derivative: (dx, dy)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=7)  # kSize -> kernelSize: sh ould be 1, 3, 5, 7


# show imgs and close
cv2.imshow('original', img)
cv2.imshow('sobel-X', sobelx)
cv2.imshow('sobel-Y', sobely)
cv2.imshow('laplacian', laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()