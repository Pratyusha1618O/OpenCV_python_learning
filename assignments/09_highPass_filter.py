#  Apply sharpening techniques using high-pass filters.
# Problem:
# Load an image using OpenCV.
# Design a high-pass filter kernel to sharpen the image.
# Apply the filter to sharpen the image.
# Display the original image and the sharpened image to compare the results.

import cv2
import numpy as np

image = cv2.imread("flower1.jpeg",0)

# high-pass filter kernel
high_pass_kernel = np.array([[0, -1, 0],
                            [-1, 5, -1],
                            [0, -1, 0]])

# Apply high-pass filter to the image
sharpened_image = cv2.filter2D(image, -1, high_pass_kernel)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()