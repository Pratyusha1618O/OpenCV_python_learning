import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the two images
img1 = cv2.imread("pic.jpg",0)
img2 = cv2.imread("flower.jpg",0)

# Resize images to the same size if needed
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# average
avg = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# add
add = cv2.add(img1, img2)

# subtract
sub = cv2.absdiff(img1, img2)

#multiply
mul = cv2.multiply(img1, img2)

# logical OR
imgOR = cv2.bitwise_or(img1, img2)

# logical AND
imgAND = cv2.bitwise_and(img1, img2)

# logical NOT
imgNOT = cv2.bitwise_not(img1, img2)


plt.figure(figsize=(15, 5))

plt.subplot(2, 4, 1)
plt.imshow(avg, cmap='gray')
plt.title('Average')

plt.subplot(2, 4, 2)
plt.imshow(add, cmap='gray')
plt.title('Add')

plt.subplot(2, 4, 3)
plt.imshow(sub, cmap='gray')
plt.title('Subtract')

plt.subplot(2, 4, 4)
plt.imshow(mul, cmap='gray')
plt.title('Multiply')

plt.subplot(2, 4, 5)
plt.imshow(imgOR, cmap='gray')
plt.title('OR')

plt.subplot(2, 4, 6)
plt.imshow(imgAND, cmap='gray')
plt.title('AND')

plt.subplot(2, 4, 7)
plt.imshow(imgNOT, cmap='gray')
plt.title('NOT')

plt.tight_layout()
plt.show()

