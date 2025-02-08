# Understand and apply edge detection using Sobel and Prewitt filters.
# Problem:
# Load an image using OpenCV.
# Apply the Sobel filter to detect edges in both horizontal and vertical directions.
# Apply the Prewitt filter to detect edges in the image.
# Display the original image and the results of edge detection using both filters.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('flower.jpg', cv2.IMREAD_GRAYSCALE)

#2. Apply the Sobel filter
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3) # Sobel in x-direction
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3) # Sobel in y-direction
sobel_edges = cv2.magnitude(sobel_x, sobel_y)  # Combine both directions


#3: Apply the Prewitt filter 
prewitt_kernel_x = np.array([[1,  0, -1],
                             [1,  0, -1],
                             [1,  0, -1]])

prewitt_kernel_y = np.array([[1,  1,  1],
                             [0,  0,  0],
                             [-1, -1, -1]])


# Convolve the image with Prewitt kernels using filter2D
prewitt_x = cv2.filter2D(image, cv2.CV_64F, prewitt_kernel_x)
prewitt_y = cv2.filter2D(image, cv2.CV_64F, prewitt_kernel_y)
prewitt_edges = cv2.magnitude(prewitt_x, prewitt_y)

#4: Display 
plt.figure(figsize=(10, 8))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Sobel edge detection
plt.subplot(2, 2, 2)
plt.imshow(sobel_edges, cmap='gray')
plt.title('Sobel Edge Detection')
plt.axis('off')

# Prewitt edge detection
plt.subplot(2, 2, 3)
plt.imshow(prewitt_edges, cmap='gray')
plt.title('Prewitt Edge Detection')
plt.axis('off')

plt.tight_layout()
plt.show()
