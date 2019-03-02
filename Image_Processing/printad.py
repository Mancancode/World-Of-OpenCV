# import the necessary packages
import imutils
import cv2
 
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("lion.jpg")
(h, w, d) = image.shape
print("width={1}, height={2}, depth={1}".format(w, h, d))
 
# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=10,y=200 at ending at x=0,y=180
# this will print Genevive Nnaji and Peet Edochie
roi = image[10:200, :180]
cv2.imshow("ROI", roi)
cv2.waitKey(0)


# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=60,y=160 at ending at x=100,y=0
# to print out Peet Edochie and Ekem Owo
roi = image[60:160, 100:]
cv2.imshow("ROI", roi)
cv2.waitKey(0)


# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=60,y=200 at ending at x=400,y=160
# to print out Peet Edochie 
roi = image[60:160, 100:160]
cv2.imshow("ROI", roi)
cv2.waitKey(0)




