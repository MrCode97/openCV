import cv2

img1 = cv2.imread('book.jpg', 0)

# Blur -> makes it less granular -> less noisy but also less detail!
img = cv2.medianBlur(img1, 3)   # second value is size


_, normalTh = cv2.threshold(img1, 128, 255, cv2.THRESH_BINARY)   # Returns two value -> '_,'


adaptiveTh_Mean = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 6)    # 11 is blockSize and 2 is parm. C

# The higher the blockSize (first value), the more detail you get but more noise. The lower -> cleaner Img but less detail
# The higher 'C' (second value), the brighter the img get. The lower -> the darker
adaptiveTh_Gaussian1 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 6)

# adaptiveTh_Gaussian7 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 6)

adaptiveTh_Gaussian_BLUR = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 6)




cv2.imshow('original', img)
cv2.imshow('original_BLUR', img1)
cv2.imshow('Normal Thresholding', normalTh)
cv2.imshow('Adaptive Mean Thresholding', adaptiveTh_Mean)
cv2.imshow('Adaptive Gaussian Thresholding1', adaptiveTh_Gaussian1)
# cv2.imshow('Adaptive Gaussian Thresholding7', adaptiveTh_Gaussian7)
cv2.imshow('Adaptive Gaussian Thresholding_BLUR', adaptiveTh_Gaussian_BLUR)

cv2.waitKey(0)
cv2.destroyAllWindows()