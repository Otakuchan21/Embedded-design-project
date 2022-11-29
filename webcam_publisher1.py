#!/usr/bin/env python

import rospy
import numpy as np
import cv2

from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError

cap = cv2.VideoCapture(0)
kernel = np.ones((2,2),np.uint8)
print(cap.isOpened())
bridge = CvBridge() 



def talker():

    pub = rospy.Publisher('/webcam', Image, queue_size=1)
    rospy.init_node('image', anonymous = False)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        gray= cv2.medianBlur(gray, 3)   #to remove salt and paper noise 
        #to binary
        ret,thresh = cv2.threshold(gray,200,255,0)  #to detect white objects
        #to get outer boundery only     
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)
        #to strength week pixels
        thresh = cv2.dilate(thresh,kernel,iterations = 5)
        im2,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours)>0:
            cv2.drawContours(frame, contours, -1, (0,255,0), 5)
            # find the biggest countour (c) by the area
            c = max(contours, key = cv2.contourArea)
            x,y,w,h = cv2.boundingRect(c)

            # draw the biggest contour (c) in green
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        if not ret:
            break

        msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        pub.publish(msg)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if rospy.is_shutdown():
            cap.release()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass