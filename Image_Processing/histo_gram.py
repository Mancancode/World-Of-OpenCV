#Histogram representation of images

#import needed libraries
import numpy as np
import imutils
from matplotlib import pyplot as plt
import cv2

image = cv2.imread("image/zex.jpg")

color = ('b','g','r')

#we now separate the color and plot each in the in the histogram
for i, col in enumerate (color):
    histogram2 = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])

    plt.show()
