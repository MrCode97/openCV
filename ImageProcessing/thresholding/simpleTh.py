import cv2 

img = cv2.imread('textT.jpg', 0)    # 0 -> geayscaled

# demo of all in openCV implemented thresholds. Note ..'_INV' means in inverted.
# cv2.threshold() returns two values(!) because of that I added another one -> _
_, binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
_, binary_inv = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
_, mask = cv2.threshold(img, 128, 255, cv2.THRESH_MASK)
_, otsu = cv2.threshold(img, 128, 255, cv2.THRESH_OTSU)
_, toZero = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO)
_, toZero_inv = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO_INV)
_, triangle = cv2.threshold(img, 128, 255, cv2.THRESH_TRIANGLE)
_, trunc = cv2.threshold(img, 128, 255, cv2.THRESH_TRUNC)

# display them
cv2.imshow('original', img)
cv2.imshow('Thresholding: binary', binary)
cv2.imshow('Thresholding: binary_inv', binary_inv)
cv2.imshow('Thresholding: mask', mask)
cv2.imshow('Thresholding: otsu', otsu)
cv2.imshow('Thresholding: toZero', toZero)
cv2.imshow('Thresholding: toZero_inv', toZero_inv)
cv2.imshow('Thresholding: triangle', triangle)
cv2.imshow('Thresholding: trunc', trunc)

cv2.waitKey(0)
cv2.destroyAllWindows()