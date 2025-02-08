import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
image = cv2.imread("flower.jpg", 0)

# Define intensity range for slicing
min_intensity = 100  # Lower bound
max_intensity = 200  # Upper bound

# Create a copy of the original image for both cases
sliced_with_bg = image.copy()
sliced_without_bg = np.zeros_like(image)  # Black background

# Apply intensity level slicing
for i in range(image.shape[0]): 
    for j in range(image.shape[1]): 
        if min_intensity <= image[i, j] <= max_intensity:
            sliced_with_bg[i, j] = 255  
            sliced_without_bg[i, j] = 255  
        else:
            sliced_with_bg[i, j] = image[i, j] 

# Display images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(sliced_with_bg, cmap='gray')
plt.title("Sliced Image (With Background)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(sliced_without_bg, cmap='gray')
plt.title("Sliced Image (Without Background)")
plt.axis("off")

plt.show()
