#import needed libraries
import numpy as np
import sys
import imutils
import argparse
import cv2

image = cv2.imread("image/tre.jpg",0)
cv2.imshow("original",image)
cv2.waitKey(0)

#Values above 127 goes to zero(black everything goes to 255(white))
tre,thresh  =   cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow("threshold Binary",thresh)
cv2.waitKey(0)
#Is a good practice to remove blur in an image b/c it reduces noise
image   =   cv2.GaussianBlur(image,(3,3),0)
cv2.waitKey(0)

#using adaptive mean threshhold
thresh   =   cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY,5,6)
cv2.imshow("Adaptive mean tresh",thresh)
cv2.waitKey(0)

#using adaptive tresh otsu
thr2    =   cv2.threshold(image,0,255, cv2.THRESH_BINARY   +   cv2.THRESH_OTSU)
cv2.imshow("Adaptive tresh otsu",thresh)
cv2.waitKey(0)


#using Gaussian Blur
blur    =   cv2.GaussianBlur(image,(5,5),0)
thr3   =  cv2.threshold(blur,0,255, cv2.THRESH_BINARY +   cv2.THRESH_OTSU)
cv2.imshow("Gaussian Blur",thresh)
cv2.waitKey(0)

