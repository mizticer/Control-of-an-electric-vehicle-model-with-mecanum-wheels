import RPi.GPIO as GPIO
import time
import threading
import sys
import Speed
import Directions
import Motor
import PID
import Detect
import Controller
import Bluetooth
import cv2
import numpy as np
import picamera
from picamera.array import PiRGBArray
from picamera import PiCamera
from PID import pid
from time import sleep

def main():
    global data
    while True:
        if Bluetooth.data == 'mecanum':
            while True:
                if Bluetooth.data == 'f':
                    Directions.forward()
                if Bluetooth.data == 'r':
                    Directions.right()
                if Bluetooth.data == 'l':
                    Directions.left()
                if Bluetooth.data == 'd':
                    Directions.down()
                if Bluetooth.data == 'fr':
                    Directions.forward_right()
                if Bluetooth.data == 'fl':
                    Directions.forward_left()
                if Bluetooth.data == 'dr':
                    Directions.down_right()
                if Bluetooth.data == 'dl':
                    Directions.down_left()
                if Bluetooth.data == 'ra':
                    Directions.right_around()
                if Bluetooth.data == 'la':
                    Directions.left_around()
                if Bluetooth.data == 'stop':
                    Directions.stop()
                if any(i.isdigit() for i in Bluetooth.data):
                    Speed.speed_of_motor(Bluetooth.data)
                if Bluetooth.data == 'normal':
                    break
                if Bluetooth.data == 'off':
                    break
                if Bluetooth.data == 'followline':
                    break
        if Bluetooth.data == 'normal':
            while True:
                if Bluetooth.data == 'f':
                    Directions.forward()
                if Bluetooth.data == 'r':
                    Directions.rightN()
                if Bluetooth.data == 'l':
                    Directions.leftN()
                if Bluetooth.data == 'd':
                    Directions.down()
                if Bluetooth.data == 'stop':
                    Directions.stop()
                if any(i.isdigit() for i in Bluetooth.data):
                    Speed.speed_of_motor(Bluetooth.data)
                if Bluetooth.data == 'mecanum':
                    break
                if Bluetooth.data == 'off':
                    break
                if Bluetooth.data == 'followline':
                    break
        if Bluetooth.data == 'followline':
            while True:
                if Bluetooth.data == 'black':
                    blackLower = (0,0,0)
                    blackUpper = (30,30,30)
                    color_track = (blackLower, blackUpper)
                elif Bluetooth.data == 'green':
                    greenLower = (17,38,0)
                    greenUpper = (92,100,34)
                    color_track = (greenLower, greenUpper)
                elif Bluetooth.data == 'red':
                    redLower = (0,0,100) 
                    redUpper = (97,79,172) 
                    color_track = (redLower, redUpper)
                elif Bluetooth.data == 'mecanum' or Bluetooth.data == 'normal' or Bluetooth.data == 'off':
                    break
                else:
                    continue
                camera = PiCamera()
                camera.resolution = (320, 240)
                rawCapture = PiRGBArray(camera, size = (320, 240))
                time.sleep(0.5)
                while True:
                    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                        image = frame.array
                        (image_out,error,detected_route)=Detect.detect_route(image, color_track)
                        cv2.imshow("Video with detected route", image_out)	
                        rawCapture.truncate(0)
                        Controller.follow_line(error,detected_route)
                        key = cv2.waitKey(1) & 0xFF	
                        if Bluetooth.data == 'mecanum' or Bluetooth.data == 'normal' or Bluetooth.data == 'off':
                            cv2.destroyAllWindows()
                            break
                    sleep(0.3) 
                    camera.close()
                    break
        if Bluetooth.data == 'off':
            GPIO.cleanup()
            sleep(0.3) 
            sys.exit()
            break
        
if __name__ == '__main__':
    thread = threading.Thread(target=Bluetooth.bluetooth_communication)
    thread.start()
    main()
