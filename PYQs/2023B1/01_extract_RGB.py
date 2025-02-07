# Take an input image and display it.
# Write a program to extract R, G, B planes from a color image. Display the output images.

import cv2
import numpy as np

img = cv2.imread("flower.jpg")

#  extract rgb 
# Split the image into R, G, B channels
B,G,R = cv2.split(img)

# Create blank images for visualization
zero_channel = np.zeros_like(B)

red_image = cv2.merge([zero_channel, zero_channel, R])
green_image = cv2.merge([zero_channel, G, zero_channel])
blue_image = cv2.merge([B, zero_channel, zero_channel])

cv2.imshow("Original image", img)
cv2.imshow("Red channel", red_image)
cv2.imshow("Green channel", green_image)
cv2.imshow("Blue channel", blue_image)


cv2.waitKey(0)
cv2.destroyAllWindows()