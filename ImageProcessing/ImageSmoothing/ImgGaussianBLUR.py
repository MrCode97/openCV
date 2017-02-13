import cv2
import numpy as np

img = cv2.imread('original.jpg')

ImgGaussianBLUR = cv2.GaussianBlur(img, (5, 5), 0, 0)   # Here '0': sigmaX & sigmaY [=standard deviation in X and Y direction]
                                                        # - if you only specify the sigmaX it takes same value for sigmaY
                                                        # - if specify the sigma = 0, then they are calculated from kernel size [Here: (5, 5)]
                                                        # source: http://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

cv2.imshow('ImgGaussianBLUR', ImgGaussianBLUR)
cv2.waitKey(0)
cv2.destroyAllWindows()