import cv2
import numpy as np

img = cv2.imread('cube.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgGray = np.float32(imgGray)                       # Makes Img float32-type, needed for cornerHarris()

# Values vary, depends on Img
dst = cv2.cornerHarris(imgGray, 2, 3, 0.04)         # ..(input, bloxkSize, ksize, k): k is free parameter (harris detection)

# Values vary, depends on Img
img[dst > 0.01 * dst.max()] = [0, 0, 255]           # draw red (0, 0, 255) corners

cv2.imwrite('dst.jpg', dst)
cv2.imwrite('Detection.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()