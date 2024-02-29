import time
import cv2 as cv

vid_capture = cv.VideoCapture(0)

while True:
    try:
        b, frame = vid_capture.read();

        cv.imshow("Frame", frame)

        key = cv.waitKey(1)

        time.sleep(0.0333) # lessen cpu strain
    except KeyboardInterrupt:
        break;