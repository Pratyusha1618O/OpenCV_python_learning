import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('pic.jpg')

# Translation
translation_matrix = np.float32([[1, 0, 100],
                                 [0, 1,  50]])

translated_img = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

plt.figure(figsize=(8,5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(translated_img, cv2.COLOR_BGR2RGB))
plt.title("Translated Image")

plt.show()