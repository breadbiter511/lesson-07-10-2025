import cv2
import numpy as np
#numpy is numerical python 

image1 = cv2.imread("otter.jpg",cv2.IMREAD_COLOR)
cv2.imshow("otter",image1)
cv2.waitKey(0)

enlargedimage = cv2.resize(image1,(900,900))
cv2.imshow("enlargedimage",enlargedimage)
cv2.waitKey(0)

reducedimage = cv2.resize(image1,(200,200))
cv2.imshow("reducedimage",reducedimage)
cv2.waitKey(0)  