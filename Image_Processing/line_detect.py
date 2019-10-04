# line_detect.py

import numpy as np
import imutils
from matplotlib import pyplot as plt
import cv2

#C odes for houghlines detection 

#load our second image
image  =   cv2.imread("image/tet.png")


# gray scale our image 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,170,apertureSize =3)

#run hough using  rho accuracy of 1 pixel
#theta accuracy of np.pi/ 180 which is one degree
#our line threshold is set to 250 (number of pionts in the line)
lines = cv2.HoughLines(edges, 1,np.pi/180,250)

#we iderate though each line and convert it to format
#reqiured by cv.lines
for rho, theta in lines [0]:
    a = np.cos (theta)
    b = np.sin (theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(image,(x1,y1),(x2,y2), (255,0,0),2)

cv2.imshow("HoughLines", image)
cv2.waitKey(0)
#cv2.destroyAllWindows()




 #C odes for probalistic line detection
  #load our second image
image  =   cv2.imread("image/tet.png")


# gray scale our image 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,170,apertureSize =3)

#using rho and theta accuracy we specify a minimuin vote
#votes piont along line of 100 and minimiun line lenght of 5 pixel
#and max gap between lines of 10 pixel
lines = cv2.HoughLines(edges, 1,np.pi/180,100,5,10)
print lines.shape

for x1,y1,x2,y2 in lines[0]:
    cv2.lines(image,(x1,y1),(x2,y2), (0,255,0),3)

cv2.imshow("probaistic", image)
cv2.waitKey(0)
cv2.destroyAllWindows()    

  
