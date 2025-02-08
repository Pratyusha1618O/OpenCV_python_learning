# Write a program to threshold an image by setting the threshold values as 0.6 × (M + N),
#  where M and N are the minimum and maximum intensity values of the image. 
# Display the input and output images.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg",0)

# Compute minimum (M) and maximum (N) intensity values
M, N = np.min(image), np.max(image)

T = 0.6 * (M + N) # threasold value

_, thresold = cv2.threshold(image, T, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", image)
cv2.imshow("Threashold", thresold)

cv2.waitKey(0)
cv2.destroyAllWindows()

