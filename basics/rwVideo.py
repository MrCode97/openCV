import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('capRecord.avi',fourcc, 5, (320, 240))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('CameraCapture', frame)
        if cv2.waitKey(1) & 0xFF == 27:     # 27 -> ESC-key
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
