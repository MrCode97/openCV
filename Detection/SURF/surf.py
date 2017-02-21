import cv2
import numpy as np

imgGRAY = cv2.imread('eagle.jpg', 0)
img = cv2.imread('eagle.jpg')

###  SURF - default Threshold
surf = cv2.xfeatures2d.SURF_create()
keyPoints, des = surf.detectAndCompute(imgGRAY, None)
imgDraw = cv2.drawKeypoints(img, keyPoints, imgGRAY, (255, 0, 0), 4)
cv2.imshow('eagle features, Threshold=default', imgDraw)
cv2.imwrite('eagle_SURF-defaultThreshold.jpg', imgDraw)
# cv2.waitKey(0)


###  SURF - Threshold=12'000
surf12 = cv2.xfeatures2d.SURF_create(12000)                 # surf new surf object
                                                            # By default (Threshold=100) I get 9018 keyPoints, great for matching but just to display now I'm looking for around 5 to 10
                                                            # So I higher the Threshold to 12'000 -> 7 local features
keyPoints12k, des = surf12.detectAndCompute(imgGRAY, None)
imgDraw = cv2.drawKeypoints(img, keyPoints12k, imgGRAY, (255, 0, 0), 4)
cv2.imshow('eagle features, Threshold=12000', imgDraw)
cv2.imwrite('eagle_SURF-12kThreshold.jpg', imgDraw)
# cv2.waitKey(0)


### U-SURF -> orientation in circles are always UP - Threshold=10'000
surfUp = cv2.xfeatures2d.SURF_create(10000)                 # create new surfUP
surfUp.setUpright(True)                                     # sets the new created 'surfUp' from default false to true -> all orientation go UP
                                                            # with: >>> surf.getUpright(True)   ..you get true or false, the set setting
keyPoints10k, des = surfUp.detectAndCompute(imgGRAY, None)
imgDraw = cv2.drawKeypoints(img, keyPoints10k, imgGRAY, (255, 0, 0), 4)
cv2.imshow('eagle features, U-SURF Threshold=10000', imgDraw)
cv2.imwrite('eagle_U-SURF.jpg', imgDraw)
# cv2.waitKey(0)

# Threshold and KeyPoints:
# By default -> Threshold = 100
print 'Threshold: ' + str(surf.getHessianThreshold())
print 'KeyPoints: ' + str(len(keyPoints))
# Threshold set to 12000
print 'Threshold: ' + str(surf12.getHessianThreshold())
print 'KeyPoints: ' + str(len(keyPoints12k))
# Threshold set to 10000
print 'Threshold: ' + str(surfUp.getHessianThreshold())
print 'KeyPoints: ' + str(len(keyPoints10k))

cv2.waitKey(0)
cv2.destroyAllWindows()
