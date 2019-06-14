#Import the Necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

image = cv2.imread("unioke.jpg")
#Code for the ArgumentParser
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", 
help = "path to where the face cascade resides") 
ap.add_argument("-i", "--image",  
help = "path to where the image file resides") 
args = vars(ap.parse_args())
image = cv2.imread(args["image"]) 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#
class FaceDetector:
    def __init__(face, faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    def detect(image, self, scaleFactore= 1.5, minNieghbor = 5,
         minSize = (30, 30)):

        react  = self.cascade.detectMultipleScale(image,
        scaleFactore = scaleFactore, minNieghbor = minNieghbor, minSize = minSize,
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

        return react  
fd = FaceDatector(args["Face"])
faceReacts = fd.detect(scale, scaleFactore= 1.5, minNieghbor = 5, minSize = (30,30))
print "I found %d face(s)"% (len(faceRects))

for (x,y,w,h) in faceReacts:
    cv2.rectangle(image, (x + y), (x+w, y+h), (0,255,0),2)
    cv2.imshow("face",image)
    cv2.waitkey(0)
