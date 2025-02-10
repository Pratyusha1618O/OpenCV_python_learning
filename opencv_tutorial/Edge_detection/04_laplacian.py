import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('flower.jpg', 0)

laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=3)
laplacian = np.uint8(np.abs(laplacian))

plt.figure(figsize=(10, 5))


plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(image, cmap='gray')

plt.subplot(1,2,2)
plt.title("Original")
plt.imshow(laplacian, cmap='gray')

plt.show()
