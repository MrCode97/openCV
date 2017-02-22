import numpy as np
import cv2

img = cv2.imread('architecture.jpg',0)

# CenSurE detector -> called "STAR detector" in openCV
star = cv2.xfeatures2d.StarDetector_create()

# BRIEF extractor
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# detect keyPoints with STAR
keyPoints = star.detect(img, None)

# compute descriptors with BRIEF
keyPoints, des = brief.compute(img, keyPoints)

print brief.descriptorSize()
print des.shape
