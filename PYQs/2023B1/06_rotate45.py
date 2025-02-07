# Read an image and display it. 
# Rotate that image with an angle of 45º in clockwise and anti-clockwise direction. 
# Display the output images.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('flower.jpg',0)

# Rotate
center = (image.shape[1] // 2, image.shape[0] // 2)
rotation_45_clock = cv2.getRotationMatrix2D(center, -45, 1) #rotate -45 clockwise
rotation_45_AntiClock = cv2.getRotationMatrix2D(center, 45, 1) #rotate 45 anti-clockwise

rotated_img_clock = cv2.warpAffine(image, rotation_45_clock, (image.shape[1], image.shape[0]))

rotated_img_anticlock = cv2.warpAffine(image, rotation_45_AntiClock, (image.shape[1], image.shape[0]))

plt.figure(figsize=(15,5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 3, 2)
plt.imshow(rotated_img_clock, cmap='gray')
plt.title("Rotated Image 45 clock")

plt.subplot(1, 3, 3)
plt.imshow(rotated_img_anticlock, cmap='gray')
plt.title("Rotated Image 45 anticlock")

plt.show()
