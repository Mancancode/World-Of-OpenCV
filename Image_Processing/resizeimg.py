 #Re-sizing of an image
#import needed libraries
import numpy as np
import imutils
from matplotlib import pyplot as plt
import cv2

#Load our image
image = cv2.imread("image/nothmen.jpg")

#Make the image 3/4 of its original size
img_scale = cv2.resize(image,None,fx=0.75,fy=0.75)
cv2.imshow("scaling-linear interpolation",img_scale)
cv2.waitKey()

#lets double the size of our image
img_scale = cv2.resize(image,None, fx=2,fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("scaling-Cubic interporlation ", img_scale)
cv2.waitKey()

#lets skew our images
img_scale = cv2.resize(image,(900,400),interpolation = cv2.INTER_AREA)
cv2.imshow("scaling-skew",img_scale)
cv2.waitKey()

cv2.distroyAllWindows()