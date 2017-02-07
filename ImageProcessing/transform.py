import cv2
import numpy as np
img = cv2.imread('chess1.jpg')

# resize-way1
way1 = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

# resize-way2
height, width = img.shape[:2]
way2 = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_CUBIC)

# shift an img
matrix = np.float32([[1,0,100],[0,1,25]])         # Here it is: [X-rightwards], [Y-downwards]
                                                # Note for GrayScaledImgs; taking rows, cols is enough (there is not more get from '.shape')
rows, cols, channels = img.shape                # Note for coloredImgs you need to take the channel as well! (altough you don't need'em here).
shift = cv2.warpAffine(img,matrix,(cols,rows))  # cv2.wrapAffine(), needs (width, height) -> '.shape' returns (height, width, channels)

# display and destroy
cv2.imshow('original', img)
cv2.imshow('way1', way1)
cv2.imshow('way2', way2)
cv2.imshow('shift', shift)
cv2.waitKey(0)
cv2.destroyAllWindows()