# Apply geometric transformations and detect shapes using the Hough transform. 
# Problem: 
# 1. Load an image and perform the following geometric transformations: 
# o Translation. 
# o Rotation. 
# o Scaling. 
# 2. Apply the Hough Line Transform to detect lines in the image. 
# 3. Draw the detected lines on the original image and display it. 

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('sudoku.png')


# Translation
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# Rotation (Rotate by 45 degrees)
center = (image.shape[1] // 2, image.shape[0] // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1)  # Rotate 45 degrees
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# Scaling (Scale the image by 1.5x)
scaled_image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

## Hough Line Transform
line_img = image.copy()
edges = cv2.Canny(image, 50, 150)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(line_img, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Red lines

# Display 
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(translated_image, cmap='gray')
plt.title("Translated Image")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(rotated_image, cmap='gray')
plt.title("Rotated Image")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(scaled_image, cmap='gray')
plt.title("Scaled Image")
plt.axis('off')

plt.figure()
plt.imshow(line_img)
plt.title("Detected Lines on Original Image")
plt.axis('off')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
