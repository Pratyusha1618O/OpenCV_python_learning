import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('krishna.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for display

# Define source and destination points for the perspective transform
points_A = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])  # Points in the original image
points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])        # Desired points in the warped image

# Compute the perspective transform matrix
M = cv2.getPerspectiveTransform(points_A, points_B)

# Apply the perspective warp
warped = cv2.warpPerspective(image, M, (420, 594))

# Plot the original and warped images
plt.figure(figsize=(20, 20))

# Original Image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

# Warped Image
plt.subplot(1, 2, 2)
plt.title("warpPerspective")
plt.imshow(warped)

# Show the plots
plt.show()
