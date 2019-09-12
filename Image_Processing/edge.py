#import needed libraries
import numpy as np
import sys
import imutils
import argparse
import cv2

image = cv2.imread("image/cri.jpg",0)


height,width = image.shape

#extract sobal Edge
Sobel_x =   cv2.Sobel(image, cv2.CV_64F,0,1,ksize=5)
Sobel_y =   cv2.Sobel(image, cv2.CV_64F,1,0,ksize=5)

cv2.imshow("original",image)
cv2.waitKey(0)
cv2.imshow("Sobel x",Sobel_x)
cv2.waitKey(0)
cv2.imshow("Sobel y",Sobel_y)
cv2.waitKey(0)

Sobel_OR    =   cv2.bitwise_or(Sobel_x,Sobel_y)
cv2.imshow("Sobel OR",Sobel_OR)
cv2.waitKey(0)

laplacian   =   cv2.Laplacian(image,cv2.CV_64F)
cv2.imshow("laplacian",laplacian)
cv2.waitKey(0)


canny   =   cv2.Canny(image,20,170)
cv2.imshow("canny",canny)
cv2.waitKey(0)

cv2.distroyAllWindows()




