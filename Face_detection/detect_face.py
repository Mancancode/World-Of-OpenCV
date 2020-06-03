#Import the Necessary packages
#Import the Necessary packages
from imutils import paths
from pyimagesearch.facedetector import FaceDetector
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

#Import the Necessary packages
#Import the Necessary packages


image = cv2.imread("unioke.jpg")
#Code for the ArgumentParser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True,
help = "path to where the face cascade resides") 
ap.add_argument("-i", "--image",  required=True,
help = "path to where the image file resides") 
args = vars(ap.parse_args())
image = cv2.imread(args["image"]) 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



fd = FaceDetector(args["Face"])
faceReacts = fd.detect(gray,scaleFactore= 1.5, minNieghbor = 5, minSize = (30,30))
print "I found %d face(s)"% (len(faceReacts))


for (x,y,w,h) in faceReacts:
    cv2.rectangle(image, (x + y), (x+w, y+h), (0,255,0),2)
    cv2.imshow("face",image)
    cv2.waitkey(0)
