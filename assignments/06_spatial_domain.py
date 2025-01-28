#  Understand and implement spatial domain filters for edge detection. 
# Problem: 
# 1. Load an image and apply convolution with a custom kernel for edge enhancement. 
# 2. Use built-in OpenCV filters to perform edge detection using: 
# o Sobel filter. 
# o Canny edge detector. 
# 3. Compare and display the original image and the results from each edge detection filter.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('flower.jpg',0)

# Apply custom kernel for edge enhancement 
sharpen_kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])

edge_enhanced_image = cv2.filter2D(image, -1, sharpen_kernel)

# Sobel filter 
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  
sobel_edges = cv2.magnitude(sobel_x, sobel_y)  

# Canny edge detector
canny_edges = cv2.Canny(image, 100, 200)

# Display
plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(edge_enhanced_image, cmap='gray')
plt.title('Edge Enhanced Image (Custom Filter)')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(sobel_edges, cmap='gray')
plt.title('Sobel Edge Detection')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(canny_edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
