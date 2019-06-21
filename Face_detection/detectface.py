
import cv2

#
class FaceDetector:
    def __init__(self, faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    def detect( self,image, scaleFactore= 1.5, minNieghbor = 5,
         minSize = (30, 30)):

        react  = self.faceCascade.detectMultipleScale(image,
        scaleFactore = scaleFactore, minNieghbor = minNieghbor, minSize = minSize,
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

        return react