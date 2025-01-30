# Apply Fourier Transform for image filtering and enhancement.
# Problem:
# Load an image using OpenCV.
# Convert the image to the frequency domain using the Fourier Transform.
# Apply a low-pass filter to remove high-frequency noise.
# Convert the image back to the spatial domain and display the filtered image.


import cv2
import numpy as np


# Load the image as grayscale
img = cv2.imread('flower.jpg', cv2.IMREAD_GRAYSCALE) 


# Compute the Fourier Transform
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)


# Create a low-pass filter
rows, cols = img.shape
crow, col_center = rows//2, cols//2
mask = np.zeros((rows, cols), np.uint8)
radius = 30  # Adjust radius for desired filtering
cv2.circle(mask, (col_center, crow), radius, 1, -1)


# Apply the filter
fshift[crow-radius:crow+radius, col_center-radius:col_center+radius] = 0


# Inverse Fourier Transform
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)


# Normalizing the image
img_norm = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
img_back_norm = cv2.normalize(img_back, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)


# Displaying the output
cv2.imshow('Input Image', img_norm)
cv2.imshow('Filtered Image', img_back_norm)
cv2.waitKey(0)
cv2.destroyAllWindows()
