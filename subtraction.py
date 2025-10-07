import cv2
import numpy as np
#numpy is numerical python

image1 = cv2.imread("otter.jpg",cv2.IMREAD_COLOR)
cv2.imshow("otter",image1)
cv2.waitKey(0)

image2 = cv2.imread("gorilla (1).jpg",cv2.IMREAD_COLOR)
cv2.imshow("gorilla",image2)
cv2.waitKey(0)

subtraction1 = cv2.subtract(image1,image2)
cv2.imshow("subtractedimage",subtraction1)
cv2.waitKey(0)

subtraction2 = cv2.subtract(image2,image1)
cv2.imshow("subtractedimage2",subtraction2)
cv2.waitKey(0)