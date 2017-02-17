import cv2
import numpy as np
# Load the colored-picture if you want to display the rectangles (from template-detecting) on the colored picture at the end.
img_rgb = cv2.imread('multiTempInput.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('multiTemp.jpg', 0)

# Take width and height
w, h = template.shape[::-1]

# Apply tempmlate-matching
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

# Draw rectangle for each detected template
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 4)

# Write Img
cv2.imwrite('multiTempResult_Thres08.jpg', img_rgb)