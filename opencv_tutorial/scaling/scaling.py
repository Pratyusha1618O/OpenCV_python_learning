import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('pic.jpg',0)
print(image.shape)

scaled_img = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
print(scaled_img.shape)

plt.figure(figsize=(8,5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(scaled_img, cmap='gray')
plt.title("Scaled Image")

plt.show()