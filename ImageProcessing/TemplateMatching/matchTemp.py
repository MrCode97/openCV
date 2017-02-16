# Note if I had managed to get 'tkinter' (needed for .pyplot) running in my virtualenv, I would have done this with matplot. 
#
# Here we are trying to match a given templete in a bigger picture with diffent in openCV implemented methods.
# If you take a good look, you will find a white or black spot on each "template-Img" (exept TM_CCORR).
# Compared to the match you will recognize that the position of those spots / cross are similar to the the template on the original picture.
# Whether they are white or black depends on if you go on 'max_loc' (i.e. TM_CCOEFF) or 'min_lock' (i.e. TM_SQDIFF): you'll see below.

import cv2
import numpy as np

img = cv2.imread('input.jpg', 0)                                            # Thats the input picture where it shall find the template
img2 = img.copy()                                                           # Useful if we want to restore the img (later)
template = cv2.imread('template.jpg', 0)                                    # for this template (picture) we are looking
w, h = template.shape[::-1]                                                 # gets width and height of the template-picture

 
# TM_SQDIFF
img = img2.copy()                                                           # Here actually not needed but "restores" img to the original picture
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)                       # apply template-matching
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)                     # cv2.minMaxLoc finds minimum and maximum values for us
top_left = max_loc                                                          # Here we take the 'max_loc'-value  => white spot / cross
bottom_right = (top_left[0] + w, top_left[1] + h)                           # we create bottom_right point to draw a rectangle
imgTM_CCOEFF = cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 3)   # we use top_left (=max_loc) and bottom_right to draw a rectangle
TM_CCOEFF = res                                                             # we "safe" res to display the diffrence between those (6) methods

# TM_CCOEFF_NORMED
img = img2.copy()
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
imgTM_CCOEFF_NORMED = cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 3)
TM_CCOEFF_NORMED = res

# TM_CCORR - did not bring the exepted result!
img = img2.copy()
res = cv2.matchTemplate(img, template, cv2.TM_CCORR)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
imgTM_CCORR = cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 3)
TM_CCORR = res

# TM_CCORR_NORMED
img = img2.copy()
res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
imgTM_CCORR_NORMED = cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 3)
TM_CCORR_NORMED = res

# TM_SQDIFF
img = img2.copy()
res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = min_loc                                                          # Best results (for TM_SQDIFF & TM_SQDIFF_NORMED) with 'min_loc'
bottom_right = (top_left[0] + w, top_left[1] + h)                           # => black spot / cross
imgTM_SQDIFF = cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 3)
TM_SQDIFF = res

# TM_SQDIFF_NORMED
img = img2.copy()
res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = min_loc                                                          # Best results (for TM_SQDIFF & TM_SQDIFF_NORMED) with 'min_loc'
bottom_right = (top_left[0] + w, top_left[1] + h)                           # => black spot / cross
imgTM_SQDIFF_NORMED = cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 3)
TM_SQDIFF_NORMED = res

# Shows how much the neighbourhood of each pixel matches with the template.
# Unfortunatly if safed they are just black or white because of that there being display and I will upload some screenshots
cv2.imshow('TM_CCOEFF.jpg', TM_CCOEFF)
cv2.imshow('TM_CCOEFF_NORMED.jpg', TM_CCOEFF_NORMED)
cv2.imshow('TM_CCORR.jpg', TM_CCORR)
cv2.imshow('TM_CCORR_NORMED.jpg', TM_CCORR_NORMED)
cv2.imshow('TM_SQDIFF.jpg', res)
cv2.imshow('TM_SQDIFF_NORMED.jpg', res)

# Shows a rectangle on the input-picture where it deteced the template
cv2.imwrite('Detection-TM_CCOEFF.jpg', imgTM_CCOEFF)
cv2.imwrite('Detection-TM_CCOEFF_NORMED.jpg', imgTM_CCOEFF_NORMED)
cv2.imwrite('Detection-TM_CCORR.jpg', imgTM_CCORR)
cv2.imwrite('Detection-TM_CCORR_NORMED.jpg', imgTM_CCORR_NORMED)
cv2.imwrite('Detection-TM_SQDIFF.jpg', imgTM_SQDIFF)
cv2.imwrite('Detection-TM_SQDIFF_NORMED.jpg', imgTM_SQDIFF_NORMED)

cv2.waitKey(0)
cv2.destroyAllWindows()