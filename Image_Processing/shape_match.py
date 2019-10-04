#shape_match.py

import numpy as np
import imutils
from matplotlib import pyplot as plt
import cv2

#load our second image
temp   =   cv2.imread("image/tet.png")
cv2.imshow("temp", temp)
cv2.waitKey(0)

#load our second image we are trying to match 
target =cv2.imread("image/huz.jpg")
target_gray = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)

#treshold the image before we start to find the contours
ret, thresh1 = cv2.threshold(temp, 277,255,0)
ret, thresh2 = cv2.threshold(target_gray, 277,255,0)


#find contours inthe temp
contours, hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#we need to sort contour by the area so we can remove 
#the largest contour wchich is the image  outline
sorted_contours = sorted(contours, key=cv2.contourArae, reverse=True)

#we then extract the kargest contours
temp_contour = contours[1]

#Extract contour from the the second image 
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SAMPLE)

#iterate through each contour and cover the bonding box
for c in contours:
    #Iterate through all the image in the target to get the match in temp using cv2.matchshapes
    match = cv2.matchshapes(temp_contours,c,1,0.0)
    print match
    #if the match valueis less than 0.15
    if match < 0.15:
        closest__contour = c
    else:
        closest__contour = []

cv2.drawContours(target,[closest_contour],-1,(0,255,0),2) 
cv2.imshow('output',target)
cv2.waitKey(0)
cv2.destroyAllWindows()   
