import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("bird.jpeg",0)

#find maximum and minimum pixel
Imin = np.min(img)
Imax = np.max(img)

# formula
stretched_img = ((img - Imin) / (Imax - Imin)) * 255

#convert to uint8
stretched_img = np.uint8(stretched_img)

#......................................................

plt.figure(figsize=(10,5))

plt.subplot(2,2,1)
plt.title("Original")
plt.imshow(img, cmap='gray')

plt.subplot(2,2,2)
plt.title("Stretched")
plt.imshow(stretched_img, cmap='gray')

plt.subplot(2,2,3)
plt.title("Histogram of original image")
plt.hist(img.ravel(), 256, [0,256], color='blue')


plt.subplot(2,2,4)
plt.title("Histogram of stretched image")
plt.hist(stretched_img.ravel(), 256, [0,256], color='blue')

plt.show()



