# Take an input image and display it.
# Write a program to perform edge detection on a greyscale image using Sobel operator. Display the output images.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg",0)

##Apply sobel operator
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = cv2.magnitude(sobel_x, sobel_y)

#display
plt.figure(figsize=(10,10))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')

plt.subplot(1,2,2)
plt.title("Sobel detected Image")
plt.imshow(sobel_edges, cmap='gray')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()