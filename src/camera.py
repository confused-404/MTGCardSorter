import time
import cv2 as cv
import numpy as np
import identifier
import os

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
        
        card_img = crop_minAreaRect(frame, rect)
        
        frame = cv.drawContours(frame, [bbox], 0, (0,0,255), 2)
        
        # find out card and more
        
        #preprocessing
        # norm_img = np.zeros((card_img.shape[0], card_img.shape[1]))
        # card_img = cv.normalize(card_img, norm_img, 0, 255, cv.NORM_MINMAX)
        card_img = resize(image=card_img, width=1000)
        # card_img = cv.fastNlMeansDenoisingColored(card_img, None, 10, 10, 7, 15)
        card_img = cv.cvtColor(card_img, cv.COLOR_BGR2GRAY)
        
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        
        card_img = cv.filter2D(card_img, -1, kernel)
        card_img = cv.threshold(card_img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
        
        cv.imwrite(img=card_img, filename=img_p)
        
        set_code = identifier.getSetCode(img_path=img_p)
        card_name = identifier.getCardName(img_path=img_p)
        
        # os.remove(img_p)
        
        frame = cv.putText(frame, card_name + " from " + set_code, (50, 50), 2, 1, (0, 255, 0), 2, cv.LINE_AA, False)
        
        cv.imshow("camera", frame)

        imgs += 1

        time.sleep(0.0333) # lessen cpu strain
    
    vid_capture.release();
    cv.destroyAllWindows();
    
    for filename in os.listdir("imgs/raw"):
        path = "imgs/raw/" + filename
        os.remove(path)
        
def crop_minAreaRect(img, rect):

   box = cv.boxPoints(rect)
   box = np.int0(box)
   width, height = int(rect[1][0]), int(rect[1][1])

   src_pts = box.astype('float32')
   dst_pts = np.array([[0, height-1], [0, 0], [width-1, 0], [width-1, height-1]], dtype='float32')
   M = cv.getPerspectiveTransform(src_pts, dst_pts)
   img_crop = cv.warpPerspective(img, M, (width, height))

   return img_crop

def resize(image, width = None, height = None, inter = cv.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized