

import numpy as np
import imutils
from matplotlib import pyplot as plt
import cv2

image   =   cv2.imread("image/tet.png")
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
#cv2.imshow("contours", image)

cv2.waitKey(0)


#======================================================================


#return all area of the objects in the image
def get_contour_areas(contours):
    all_areas=[]
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

#load our image 
image = cv2.imread("images/tet.jpg")
original_img = image

#ok now let print our contours area before we sort them
print'our contour before sorting'
print get_contour_areas(contours)

#sort contours from large to small with the reverse=True, when is False it sorts opposite
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

print'our contour after sorting'
print get_contour_areas(sorted_contours)

#Iterate on it each contourand draw on them one at a time
for c in sorted_contours:
    cv2.drawContours(original_img,[c],-1,(255,0,0),3)
    cv2.waitKey(0)
    cv2.imshow('count',original_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

