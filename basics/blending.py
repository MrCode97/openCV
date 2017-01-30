import cv2
import numpy as np

man = cv2.imread('man.jpg')
matches = cv2.imread('matches.jpg')
heightMan, widthMan, channelsMan = man.shape                        #takes resolution
img = np.zeros((heightMan, widthMan, channelsMan), np.uint8)        #generates black-plane with same resolution as picture [man.jpg]

i = 0
while i <= 630:
    heightMatches, widthMatches, channelsMatches = matches.shape
    width = widthMatches-widthMan
    img = matches[0:heightMan, width-i:widthMatches-i]              #create new snippet [1pixel more right than before] from 'matches.jpg'
    img = cv2.addWeighted(img, 0.4, man, 0.2, 0)                    #blending -> pictures must have same resolution!

    i = i+1

    cv2.imshow('blending', img)
    cv2.waitKey(5)

cv2.destroyAllWindows()
