# Apply various thresholding techniques for image segmentation.
# Problem:
# Load a grayscale image using OpenCV.
# Apply global thresholding to segment bright and dark regions.
# Apply adaptive thresholding to handle varying lighting conditions in the image.
# Display the original image and the thresholded images obtained using global and adaptive thresholding.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('flower.jpg', 0)

##1 Apply global thresholding
_, global_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

##2 Apply adaptive thresholding
adaptive_thresh_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adaptive_thresh_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

##4 Display
plt.figure(figsize=(10, 8))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Global Thresholding
plt.subplot(2, 2, 2)
plt.imshow(global_thresh, cmap='gray')
plt.title('Global Thresholding')
plt.axis('off')

# Adaptive Thresholding (Mean)
plt.subplot(2, 2, 3)
plt.imshow(adaptive_thresh_mean, cmap='gray')
plt.title('Adaptive Thresholding (Mean)')
plt.axis('off')

# Adaptive Thresholding (Gaussian)
plt.subplot(2, 2, 4)
plt.imshow(adaptive_thresh_gaussian, cmap='gray')
plt.title('Adaptive Thresholding (Gaussian)')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
