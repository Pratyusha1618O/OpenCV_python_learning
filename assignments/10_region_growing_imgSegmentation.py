#  Use region-growing techniques for image segmentation.
# Problem:
# Load a grayscale image using OpenCV.
# Apply a region-growing algorithm to segment areas of similar intensity.
# Highlight the segmented regions on the original image.
# Display the original image and the segmented image.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the grayscale image
image = cv2.imread('flower2.jpg', cv2.IMREAD_GRAYSCALE)

# Step 2: Region-growing function
def region_growing(image, seed, threshold=15):
    # Initialize variables
    rows, cols = image.shape
    segmented = np.zeros_like(image)  # Binary segmented image
    visited = np.zeros_like(image, dtype=bool)  # To keep track of visited pixels
    
    # Define the 4-connected neighbors (up, down, left, right)
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Initialize the seed point
    seed_value = image[seed]
    segmented[seed] = 255  # Mark the seed as part of the region
    visited[seed] = True
    
    # List to store the pixels to check
    to_check = [seed]
    
    # Region-growing process
    while to_check:
        x, y = to_check.pop(0)
        
        # Check all 4-connected neighbors
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx, ny]:
                # If the intensity difference is within the threshold, grow the region
                if abs(int(image[nx, ny]) - int(seed_value)) < threshold:
                    segmented[nx, ny] = 255  # Add to the region
                    visited[nx, ny] = True  # Mark as visited
                    to_check.append((nx, ny))  # Add to the list of pixels to check
    
    return segmented

# Step 3: Select a seed point (you can choose any point in the image)
seed_point = (100, 100)  # Example seed point; you can change this as needed

# Step 4: Apply the region-growing algorithm
segmented_image = region_growing(image, seed_point, threshold=15)

# Step 5: Highlight the segmented region on the original image (optional)
highlighted_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert to BGR to overlay
highlighted_image[segmented_image == 255] = [0, 0, 255]  # Highlight region in red

# Step 6: Display the original and segmented images
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Segmented Image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(highlighted_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
plt.title('Segmented Image (Region Growing)')
plt.axis('off')

plt.tight_layout()
plt.show()
