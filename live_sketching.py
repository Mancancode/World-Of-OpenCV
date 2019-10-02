#import needed libraries
import numpy as np
import sys
import imutils
import argparse
import cv2

#create our sketching function
def sketch(image):
    #convert image to grayscale
    img_gray    =   cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #clean up the blur using Gussian blue
    img_gray_bur    =   cv2.GaussianBlur(img_gray,(5,5),0)

    #Detect thre edges using canny
    canny_egde  =   cv2.Canny(img_gray_bur,30,65)

    #Do an invert to binarize the image
    ret,mask    =   cv2.threshold(canny_egde,60,255,cv2.THRESH_BINARY_INV)
    return mask
      #capture the webcam
cap =   cv2.VideoCapture(0)

while True:
    ret, frame  =   cap.read()
    cv2.imshow("Live sketching stream",sketch(frame))
    if cv2.waitKey(1)==13:
        break

#Release camera and close windows
cap.release()
cv2.desroyAllWindows







