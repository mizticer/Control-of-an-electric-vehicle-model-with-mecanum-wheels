import cv2
import numpy as np

def detect_route(image, color_track):
    colorline = cv2.inRange(image, color_track[0], color_track[1]) 
    kernel = np.ones((3,3), np.uint8)
    colorline = cv2.erode(colorline, kernel, iterations=5)
    colorline = cv2.dilate(colorline, kernel, iterations=9)
    contours_detected, hierarchy_blk = cv2.findContours(colorline,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_detected) > 0 :
        rectangle = cv2.minAreaRect(contours_detected[0])
        (x, y) = rectangle[0]
        setpoint = 160
        error = int(x - setpoint) 
        box = cv2.boxPoints(rectangle)
        box = np.int0(box)
        cv2.drawContours(image,[box],0,(0,255,255),3)	 
        cv2.putText(image,str(error),(10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,255), 2)
        cv2.line(image, (int(x),200 ), (int(x),250 ), (0,255,255),3)
        return image, error, len(contours_detected)
    if len(contours_detected) == 0 :
        cv2.putText(image,str("NOT DETECTED"),(40, 120), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
        return image, 0, len(contours_detected)
