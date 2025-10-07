import cv2
import numpy as np
#numpy is numerical python

image1 = cv2.imread("face1.jpg",cv2.IMREAD_COLOR)
cv2.imshow("facw1",image1)
cv2.waitKey(0)

image2 = cv2.imread("face2.jpg",cv2.IMREAD_COLOR)
cv2.imshow("face2",image2)
cv2.waitKey(0)

sumofimages = cv2.addWeighted(image1,0.5,image2,0.5,0)
cv2.imshow("combined",sumofimages)
cv2.waitKey(0)  

sumofimages2 = cv2.addWeighted(image1,0.7,image2,0.3,0)
cv2.imshow("combined2",sumofimages2)
cv2.waitKey(0)  

sumofimages3 = cv2.addWeighted(image1,0.3,image2,0.7,0)
cv2.imshow("combined3",sumofimages3)
cv2.waitKey(0)  