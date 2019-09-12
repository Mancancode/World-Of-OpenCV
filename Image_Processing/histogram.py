#Histogram representation of images

#import needed libraries
import numpy as np
import imutils
from matplotlib import pyplot as plt
import cv2

image = cv2.imread("image/xez.jpg")
histogram = cv2.calcHist([image],[0],None,[256],[0, 256])

#We now plot a histogram ravels to flaten our image
plt.hist(image.ravel(),256,[0,256]); plt.show()

#Viewing separates color channels
color = ('b','g','r')

#we now separate the color and plot each in the in the histogram
for i, col in enumerate (color):
    histogram2 = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])

    plt.show()
