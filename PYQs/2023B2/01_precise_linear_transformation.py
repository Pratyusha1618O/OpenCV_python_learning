# Write a program to perform contrast stretching on a greyscale image using piecewise linear transformation operation. 
# Display the output.

import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
    Apply piecewise linear transformation for contrast stretching.
    :param img: Input grayscale image
    :param r1, s1, r2, s2: Control points for transformation
    :return: Contrast-stretched image
"""

image = cv2.imread("flower.jpg")

r1, s1 = 50,30
r2, s2 = 180, 220


# Create a lookup table for pixel mapping
lookup_table = np.zeros(256, dtype = np.uint8)

for i in range(256):
    if i<r1:
        lookup_table[i] = (s1 / r1) * i
    elif i < r2:
        lookup_table[i] = ((s2 - s1) / (r2 - r1)) * (i - r1) + s1
    else:
        lookup_table[i] = ((255 - s2) / (255 - r2)) * (i - r2) + s2

stretched_image = cv2.LUT(image, lookup_table)

cv2.imshow("Original image", image)
cv2.imshow("Stretched image", stretched_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


