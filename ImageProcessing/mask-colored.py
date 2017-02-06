import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()

    # bgr to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range in red:  Format: HSV=[hue, saturation, value]      ->cheatsheet for more info.
    lower_red = np.array([0,100,100])
    upper_red = np.array([20,255,255])

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # cuts the mask out from the original frame and creates object
    colored = cv2.bitwise_and(frame, frame, mask= mask)

    #display cam-frame and "masked"-frame
    cv2.imshow('frame',frame)
    cv2.imshow('hsv-frame', hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('red-black mask', colored)
    k = cv2.waitKey(5) & 0xFF

    if k == ord('s'):
        cv2.imwrite('mask-colored_original-frame.jpg', frame)
        cv2.imwrite('mask-colored_convertet-frame_HSV.jpg', hsv)
        cv2.imwrite('mask-colored_masked-frame.jpg', mask)
        cv2.imwrite('mask-colored_colored-mask.jpg', colored)

    if k == 27:
        break

cv2.destroyAllWindows()
