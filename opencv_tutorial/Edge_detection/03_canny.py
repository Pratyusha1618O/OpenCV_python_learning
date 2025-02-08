import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('flower.jpg', 0)

# canny edge detection
canny = cv2.Canny(image, 100, 200) #(image, low thresold, high thresold)

plt.figure(figsize=(10, 5))

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(image, cmap='gray')

plt.subplot(1,2,2)
plt.title("Original")
plt.imshow(canny, cmap='gray')

plt.show()