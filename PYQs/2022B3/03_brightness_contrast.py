# 3. Write a program to perform the following image enhancement methods :
# (a) Brightness enhancement
# (b) Contrast manipulation.
# Display the output images.


import cv2
import numpy as np

image = cv2.imread("pic.jpg")


# (a) Brightness Enhancement
brightness_value = 50 
brightened_image = cv2.convertScaleAbs(image, alpha=1, beta=brightness_value)

# (b) Contrast Manipulation
contrast_value = 1.5
contrasted_image = cv2.convertScaleAbs(image, alpha=contrast_value, beta=0)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Brightness Enhanced", brightened_image)
cv2.imshow("Contrast Manipulated", contrasted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
