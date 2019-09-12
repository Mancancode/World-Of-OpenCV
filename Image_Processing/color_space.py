#Exploring looking at individual colors
#import needed libraries

import numpy as np
import sys
import cv2

#load image
image = cv2.imread("image/kee.jpeg")

#opencv splite functions splite image in diffrent index
B, G, R = cv2.split(image)

print B.shape
cv2.imshow("red", R)
cv2.imshow("green", G)
cv2.imshow("blue", B)
cv2.waitKey(0)


#Now Merge all to get the original images
merge = cv2.merge([B,G,R])
cv2.imshow("Merged",merge)

#Now let applify the colors
merged = cv2.merge([B+100,G+100,R])
cv2.imshow("Amplified Image",merged)
cv2.waitKey(0)



#using spite functions to see the actual colores

#We create a matrix of zeros
# with the dimention of h x w
zeros = np.zeros(image.shape[:2], dtype = "uint8") 
cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))

cv2.waitKey(0)
cv2.distroyAllWindows()
