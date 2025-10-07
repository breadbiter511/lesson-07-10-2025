import cv2
import numpy as np
#numpy is numerical python

image1 = cv2.imread("otter.jpg",cv2.IMREAD_COLOR)
cv2.imshow("otter",image1)
cv2.waitKey(0)

image2 = cv2.imread("gorilla (1).jpg",cv2.IMREAD_COLOR)
cv2.imshow("gorilla",image2)
cv2.waitKey(0)

conversion = np.ones((10,10),np.uint8)
erodedimage = cv2.erode(image2,conversion)
cv2.imshow("new image ",erodedimage)
cv2.waitKey(0)

conversion = np.ones((10,10),np.uint8)
erodedimage2 = cv2.erode(image1,conversion)
cv2.imshow("new image 2 ",erodedimage2)
cv2.waitKey(0)