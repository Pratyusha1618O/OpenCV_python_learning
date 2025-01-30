#  Use region-growing techniques for image segmentation.
# Problem:
# Load a grayscale image using OpenCV.
# Apply a region-growing algorithm to segment areas of similar intensity.
# Highlight the segmented regions on the original image.
# Display the original image and the segmented image.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('box.jpg',0)

# Region-growing function
def region_growing(image, seed, threshold=15):
    rows, cols = image.shape
    segmented = np.zeros_like(image)  
    visited = np.zeros_like(image, dtype=bool)  
    
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    #seed point
    seed_value = image[seed]
    segmented[seed] = 255 
    visited[seed] = True
    
    to_check = [seed]
    
    # Region-growing process
    while to_check:
        x, y = to_check.pop(0)
        
        # Check all 4-connected neighbors
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx, ny]:
                if abs(int(image[nx, ny]) - int(seed_value)) < threshold:
                    segmented[nx, ny] = 255 
                    visited[nx, ny] = True 
                    to_check.append((nx, ny))  
    
    return segmented

# Select a seed point
seed_point = (100, 100)

# region-growing algorithm
segmented_image = region_growing(image, seed_point, threshold=15)


highlighted_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  
highlighted_image[segmented_image == 255] = [0, 0, 255]  # Highlight region in red

# Display
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Segmented Image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(highlighted_image, cv2.COLOR_BGR2RGB)) 
plt.title('Segmented Image (Region Growing)')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
