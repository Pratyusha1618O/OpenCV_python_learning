import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
image = cv2.imread("flower.jpg", cv2.IMREAD_GRAYSCALE)
mask = np.zeros_like(image)

# Seed point and threshold
seed = (100, 100)  # Change if needed
threshold = 10
stack = [seed]

while stack:
    x, y = stack.pop()
    if mask[x, y] == 0:
        mask[x, y] = 255  # Mark as visited
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < image.shape[0] and 0 <= ny < image.shape[1]:
                if abs(int(image[nx, ny]) - int(image[x, y])) < threshold:
                    stack.append((nx, ny))

# Display images
cv2.imshow("Original", image)
cv2.imshow("Segmented image", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
