# Assignment 13: Pixel Classification Using Local Thresholding
# Description: Perform pixel classification using local thresholding.
# Problem:
# Load a grayscale image using OpenCV.
# Apply local thresholding to segment different regions based on local intensity variations.
# Highlight the classified regions in the image using different colors.
# Display the original image and the classified image.


import cv2
import numpy as np

def local_thresholding(image, block_size=15, offset=10):
    rows, cols = image.shape
    thresholded_image = np.zeros((rows, cols), dtype=np.uint8)

    for i in range(0, rows, block_size):
        for j in range(0, cols, block_size):
            x1 = max(0, i)
            y1 = max(0, j)
            x2 = min(i + block_size, rows)
            y2 = min(j + block_size, cols)

            local_region = image[x1:x2, y1:y2]
            threshold = np.mean(local_region) - offset
            thresholded_image[x1:x2, y1:y2] = ((local_region > threshold) * 255).astype(np.uint8)

    return thresholded_image

# Load image
img = cv2.imread('flower.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Apply local thresholding
thresholded_img = local_thresholding(img, block_size=15, offset=10)

# Display images
cv2.imshow('Original Image', img)
cv2.imshow('Classified Image', thresholded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
