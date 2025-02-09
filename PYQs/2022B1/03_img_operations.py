# Write a program to perform the following operations on a greyscale image - 
# (i) Image Negative,
# (ii) Image thresholding. 
# Display the output images.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("pic.jpg",0)

# 1. Image negative
negative_img = 255 - image # Invert pixel values

# 2. Thresholding
threshold_value = 127
_, thresolded_img = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# 3. Adaptive thresolding
adaptive_threshold_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

adaptive_threshold_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


plt.figure(figsize=(15, 5))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(negative_img, cmap='gray')
plt.title('Negative')

plt.subplot(2, 3, 3)
plt.imshow(thresolded_img, cmap='gray')
plt.title('Global thresold')

plt.subplot(2, 3, 4)
plt.imshow(adaptive_threshold_mean, cmap='gray')
plt.title('Adaptive Thresholding (mean)')

plt.subplot(2, 3, 5)
plt.imshow(adaptive_threshold_gaussian, cmap='gray')
plt.title('Adaptive Thresholding (gaussian)')

plt.tight_layout()
plt.show()
