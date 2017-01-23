import numpy as np
import cv2

# read / load image
img = cv2.imread('bubble.jpg', 0)

# display image
cv2.namedWindow('OpenCV - Bubble', cv2.WINDOW_NORMAL)
cv2.imshow('OpenCV - Bubble', img)

key = cv2.waitKey(0) & 0xFF     # 64bit -> 0xFF

if key == 27:                   # 27 = ESC-Key
    cv2.destroyAllWindows()
elif key == ord('s'):           # s
    # save image
    cv2.imwrite('bubble-grayscaled.jpg', img)
    cv2.destroyAllWindows()
