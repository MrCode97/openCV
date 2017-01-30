import cv2
import numpy as np

img = cv2.imread('chess1.jpg')
cv2.imshow('original', img)

default = cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_DEFAULT)
cv2.imshow('default', default)
cv2.imwrite('border_default.jpg', default)

#---same as cv2.BORDER_DEFAULT---
reflect = cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_REFLECT)
cv2.imshow('reflect', reflect)
cv2.imwrite('border_reflect.jpg', reflect)

# ---can't see a differenece there (compared to cv2.BORDER_REFLECT)---
#reflect101 = cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_REFLECT101)
#cv2.imshow('reflect101', reflect101)

replicate= cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
cv2.imshow('replicate', replicate)
cv2.imwrite('border_replicate.jpg', replicate)

constant = cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value=[255, 255, 255])  # def color; 255, 255, 255 [=white]
cv2.imshow('constant', constant)
cv2.imwrite('border_constant.jpg', constant)

wrap = cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_WRAP)
cv2.imshow('wrap', wrap)
cv2.imwrite('border_wrap.jpg', wrap)

isolated = cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_ISOLATED)
cv2.imshow('isolated', isolated)
cv2.imwrite('border_isolated.jpg', isolated)

#---error---
#transparent= cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_TRANSPARENT)
#cv2.imshow('transparent', transparent)

cv2.waitKey(0)
cv2.destroyAllWindows()
