# Write a program to enhance an image using Histogram Equalization method.
# Display histograms of the input and output images.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg",0)

if image is None:
    print("Error: Could not read the image.")
    exit()

# Histogram Equalization
equ = cv2.equalizeHist(image)

#plot the histogram of an image
def plot_histogram(image, title):
    plt.hist(image.ravel(), bins=256, range=(0, 256), color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel('pixel intensity')
    plt.ylabel('frequency')


plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.title("Original image")
plt.imshow(image, cmap='gray')

plt.subplot(2,2,2)
plt.title("Equalized image")
plt.imshow(equ, cmap='gray')

plt.subplot(2,2,3)
plot_histogram(image, 'Input image histogram')

plt.subplot(2,2,4)
plot_histogram(equ, 'Output image histogram')

plt.show()
