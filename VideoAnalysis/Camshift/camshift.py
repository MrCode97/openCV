import numpy as np
import cv2
cap = cv2.VideoCapture('Slw.mp4')

# take first frame of the video
ret, frame = cap.read()

# setup initial location of window
# setup initial location of window -> in this example don't detect but we set the object to track (only on first frame) by given coordinates.
r, h, c, w = 82, 50, 69, 94 # r = yPoint-topLeft-rectangle [y-axis](row?),
                            # h = height of rectange(tracked-object),
                            # c= xPoint-topLeft-rectangle x-axis (cols?),
                            # w = width of rectangle (tracked object)
                            # 0------>X
                            # |
                            # |
                            # Y
track_window = (c, r, w, h)

# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]                                                       # def region by given coordinates (see above)
hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)                                 # convert bgr to hsv
mask = cv2.inRange(hsv_roi, np.array((0, 60, 32)), np.array((180, 255, 255 )))  # create mask and leave some low-light values
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])                  # calculate Histogram
                                                                                # cv2.calcHist(images, channels, mask, histSize, ranges, [hist, accumulate])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
while(1):
    ret ,frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply meanshift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        # Draw it on image
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame,[pts],True, 255,2)
        cv2.imshow('img2',img2)
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite(chr(k)+".jpg",img2)
    else:
        break
cv2.destroyAllWindows()
cap.release()
