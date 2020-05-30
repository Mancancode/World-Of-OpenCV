import cv2
import os as sys

#get supplied values
imagePath = sys.args[1]
cascPath = sys.args[2]


#Creat the haar cascading
faceCascade = cv2.CreatascadeClifier(cascPath)
image = cv2.mimread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Detect faces in the image
faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbor=5, minSize = (30,30), flags = cv2.cv.CV_HAAR_IMAGE
)
print "fOUND {0} faces".format(len(faces))

#Draw a rectangle around the faceCascade
for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y),(x+w, y+h), (0,255,0), 2)

cv2.imshow("faces found",image)
cv2.waitkey(0)


