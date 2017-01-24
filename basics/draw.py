import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (128, 384), (384, 384), (255, 255, 255), 2)

cv2.rectangle(img, (136, 350), (376, 370), (0, 0, 255), 1)

cv2.circle(img, (256, 180), 120, (0, 145, 200), -1)
cv2.circle(img, (206, 175), 20, (0, 0, 0), -1)
cv2.circle(img, (312, 175), 20, (0, 0, 0), -1)

cv2.ellipse(img, (256, 100), (192, 45), 0, 0, 360, (0, 150, 220), -1)
cv2.ellipse(img, (256, 246), (60, 30), 0, 0, 180, (0, 0, 0), -1)

points = np.array([[216, 306], [296, 306], [270, 320], [256,346], [242, 320]], np.int32)
#points = points.reshape((-1, 1, 2))
cv2.polylines(img, [points], True, (255, 255, 255))

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, 'OpenCV', (128, 124), font, 2.2, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'Profilwochen', (180, 366), 5, 1, (255, 255, 255), 1, cv2.LINE_AA)

cv2.imshow('picture', img)
cv2.imwrite('openCVdrawing.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
