import cv2
import numpy as np
# mouse callback function
def draw_geom(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img, (x-25, y-25), (x+25, y+25), (0, 255, 0), 5)

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 50, (255, 0, 0), -1)


img = np.zeros((720, 1024, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_geom)

while(True):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.imwrite('persDrawing.jpg', img)
cv2.destroyAllWindows()
