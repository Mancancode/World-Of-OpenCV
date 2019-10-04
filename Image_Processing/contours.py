#COPY & PASTE{     python contours.py      }TO RUN THE CODE
#import needed libraries
import numpy as np
import imutils
from matplotlib import pyplot as plt
import cv2

image   =   cv2.imread("image/tre.jpg")
#cv2.imshow("tet_image",image)
#cv2.waitKey(0)

#Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#canny edge
edge = cv2.Canny(gray,30,200)
#cv2.imshow("Canny edge",edge)
#cv2.waitKey(0)

#Make the image black
black_img = np.zeros((image.shape[0], image.shape[1],3))

#To find contours we use copy of the image (edged.copy) since the contours alters image
contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#cv2.imshow("canny img after contouring", edge)
#cv2.waitKey(0)

#print the number of contours
print"number of contour found  " + str(len(contours))

#Drow lines on the black contours
cv2.drawContours(black_img,contours,-1,(0,255,0),5)
#cv2.imshow("black contours",black_img)

#Drow all contours using -1 as the 3rd parameter to draw all
cv2.drawContours(image,contours,-1,(0,255,0),5)
cv2.imshow("contours", image)

#iterate through each contour and compute the appx contours 
for c in contours:
    #calculate accuracy as a persent of the contours perimeters
    accuracy = 0.00 * cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,accuracy,True)
    cv2.drawContours(image,[approx],0,(0,(255),0),2)
    cv2.imshow("accuracy",image)

cv2.waitKey(0)
cv2.destroyAllWindows()