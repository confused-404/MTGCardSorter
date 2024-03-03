import time
import cv2 as cv

vid_capture = cv.VideoCapture(0)

imgs = 0

while not (cv.waitKey(1) & 0xFF == ord('q')):
    b, frame = vid_capture.read();
    
    cv.imshow("Frame", frame)

    # cv.imwrite("imgs\\frame" + str(imgs) + ".jpg", frame)

    imgs += 1

    # time.sleep(0.0333) # lessen cpu strain

vid_capture.release();
cv.destroyAllWindows();