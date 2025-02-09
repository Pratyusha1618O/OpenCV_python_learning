# Write a program to perform colour separation into R, G and B from a colour image. 
# Then use these R, G and B to convert the original colour image to its equivalent greyscale image. 
# Display output images.

import cv2
import numpy as np

img = cv2.imread("pic.jpg")

B, G, R = cv2.split(img)

zero_channel = np.zeros_like(B)

red = cv2.merge([zero_channel, zero_channel, R])
green = cv2.merge([zero_channel, G, zero_channel])
blue = cv2.merge([B, zero_channel, zero_channel])

cv2.imshow("Original", img)
cv2.imshow("Red", red)
cv2.imshow("Green", green)
cv2.imshow("Blue", blue)

img_again = cv2.merge((B,G,R))
cv2.imshow("Image merged", img_again)

cv2.imshow("Grayscale", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))


cv2.waitKey(0)
cv2.destroyAllWindows()