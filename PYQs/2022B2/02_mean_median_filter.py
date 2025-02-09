# Write a program to enhance an image using mean filtering and median filtering. Display the output images.

import cv2
import numpy as np

image = cv2.imread("pic.jpg")

# mean filter
ksize = (5,5)
mean = cv2.blur(image, ksize)
cv2.imshow("Mean filter", mean)

# median filter
median = cv2.medianBlur(image, 5)
cv2.imshow("median filter", median)



cv2.waitKey(0)
cv2.destroyAllWindows()