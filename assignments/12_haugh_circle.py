# Assignment 12: Hough Circle Transform for Circle Detection
# Description: Detect circles in an image using the Hough Circle Transform.
# Problem:
# Load an image with circular shapes.
# Apply the Hough Circle Transform to detect circles in the image.
# Draw the detected circles on the original image.
# Display the original image with the detected circles.


import cv2
import numpy as np


img = cv2.imread('fruit.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original Image',img)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)


if circles is not None:
    circles = np.uint16(np.around(circles))


    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)


cv2.imshow('Detected Circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
