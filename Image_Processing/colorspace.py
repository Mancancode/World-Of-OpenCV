#import needed libraries
#import needed libraries
#import needed libraries
import numpy as np
import sys
import imutils
import argparse
import cv2




image = cv2.imread("image/jaw.jpg")
                     
  
#import needed libraries
  
#Color filtering 
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv_image",hsv_image)
cv2.imshow("HUE channel",hsv_image[:,:,0])
cv2.imshow("SATURATED channel",hsv_image[:,:,1])
cv2.imshow("VALUE channel",hsv_image[:,:,2])

#Display image and wiat till crash key is activated
cv2.waitKey(0)
cv2.distroyAllWindows()
