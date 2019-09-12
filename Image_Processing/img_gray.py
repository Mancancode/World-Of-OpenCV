#import needed libraries
import numpy as np
import sys
import imutils
import cv2

#Load our image 
img = cv2.imread('image/jew.jpg',0)

#print the image grayscale
cv2.imshow("Grayscale",img)
cv2.waitKey()
cv2.distroyAllWindows()