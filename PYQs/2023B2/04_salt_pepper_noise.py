import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

image = cv2.imread("flower.jpg",0)

noisy_img = image.copy()

salt_prob = 0.02
pepper_prob = 0.02

total_pixel = image.size

#add salt
salt = int(total_pixel * salt_prob)
for i in range(salt):
    i = random.randint(0, image.shape[0] - 1) #random row
    j = random.randint(0, image.shape[1] - 1) #random column
    noisy_img[i, j] = 255 # Set pixel to white

#add pepper
pepper = int(total_pixel * pepper_prob)
for i in range(pepper):
    i = random.randint(0, image.shape[0] - 1) #random row
    j = random.randint(0, image.shape[1] - 1) #random column
    noisy_img[i, j] = 0 # Set pixel to black

# median filter
m3 = cv2.medianBlur(noisy_img, 3)
m5 = cv2.medianBlur(noisy_img, 5)
m7 = cv2.medianBlur(noisy_img, 7)

plt.figure(figsize=(15, 8))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")

plt.subplot(2, 3, 2)
plt.imshow(noisy_img, cmap='gray')
plt.title("Image with Salt & Pepper Noise")

plt.subplot(2, 3, 3)
plt.imshow(m3, cmap='gray')
plt.title("Filtered (3x3)")

plt.subplot(2, 3, 4)
plt.imshow(m5, cmap='gray')
plt.title("Filtered (5x5)")

plt.subplot(2, 3, 5)
plt.imshow(m7, cmap='gray')
plt.title("Filtered (7x7)")

plt.show()