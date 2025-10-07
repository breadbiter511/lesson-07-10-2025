import cv2
import numpy as np
#numpy is numerical python

image1 = cv2.imread("Tennis_Ball.jpg",cv2.IMREAD_COLOR)
cv2.imshow("tennis",image1)
cv2.waitKey(0)

image2 = cv2.imread("Cup (1).jpg",cv2.IMREAD_COLOR)
cv2.imshow("cup",image2)
cv2.waitKey(0)

conversion = np.ones((40,40),np.uint8)
erodedimage = cv2.erode(image2,conversion)
cv2.imshow("new image ",erodedimage)
cv2.waitKey(0)

conversion = np.ones((20,20),np.uint8)
erodedimage2 = cv2.erode(image1,conversion)
cv2.imshow("new image 2 ",erodedimage2)
cv2.waitKey(0)