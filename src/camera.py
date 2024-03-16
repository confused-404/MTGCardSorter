import time
import cv2 as cv
import numpy as np

def start_camera():
    vid_capture = cv.VideoCapture(0)
    imgs = 0

    while not (cv.waitKey(1) & 0xFF == ord('q')):
        b, frame = vid_capture.read();
        
        # cv.imshow("Frame", frame)

        img_p = "imgs/raw/card" + str(imgs) + ".jpg"

        # cv.imwrite(img_p, img=frame)
        
        # get bounding box of image
        
        pro_img = frame.copy()
        pro_img = cv.cvtColor(pro_img, cv.COLOR_BGR2GRAY)
        
        ret, bin_img = cv.threshold(pro_img, 127, 255, 0)
        
        contours, _ = cv.findContours(bin_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)
        
        cnt = contours[1]
        
        rect = cv.minAreaRect(cnt)
        bbox = cv.boxPoints(rect)
        bbox = np.int0(bbox)
        
        frame = cv.drawContours(frame, [bbox], 0, (0,0,255), 2)
        
        cv.imshow("camera", frame)

        imgs += 1

        time.sleep(0.0333) # lessen cpu strain
    
    vid_capture.release();
    cv.destroyAllWindows();

