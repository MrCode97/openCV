import numpy as np
import cv2

img = cv2.imread('bubble.jpg')

bubble = img[440:1240, 635:1435]        #[height1:heigt2, width1:width2]
img[0:800, 0:800] = bubble

cv2.imshow('doubleBubble', img)
cv2.imwrite('doubleBubble.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
