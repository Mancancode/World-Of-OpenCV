#import needed libraries
import numpy as np
import sys
import imutils
import argparse
import cv2

#Load our image 
image = cv2.imread("image/kee.jpeg")
cv2.imshow("Original", image)
cv2.waitKey(0)
 
# convert the image to grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray_img)
cv2.waitKey(0)
cv2.distroyAllWindows()
