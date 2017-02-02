import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()

    # bgr to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range in green:  Format: HSV=[hue, saturation, value]      ->cheatsheet for more info.
    lower_green = np.array([40,30,30])
    upper_green = np.array([70,120,125])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    #display cam-frame and "masked"-frame
    cv2.imshow('frame',frame)
    cv2.imshow('hsv-frame', hsv)
    cv2.imshow('mask',mask)
    k = cv2.waitKey(5) & 0xFF

    if k == ord('s'):
        cv2.imwrite('mask_original-frame.jpg', frame)
        cv2.imwrite('mask_convertet-frame_HSV.jpg', hsv)
        cv2.imwrite('mask_masked-frame.jpg', mask)

    if k == 27:
        break

cv2.destroyAllWindows()
