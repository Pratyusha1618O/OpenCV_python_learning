# Take an input image and display it.
# Write a program to add Gaussian noise to an image. Then perform noise reduction using simple Arithmetic Mean filter. 
# The original image should be greyscale. Display the output images.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg",0)

if image is None:
    print("Error! image not found.")
    exit()

# Add Gaussian noise
mean = 0 # mean of gaussian noise
sigma = 25 #standard daviation (controls noise level)
noise = np.random.normal(mean, sigma, image.shape) # generate noise
noisy_img = image + noise # add vnoise to image
noisy_img = np.clip(noisy_img, 0, 255) # keep pixel value in range 0-255
noisy_img = np.uint8(noisy_img) # conver to int type


## Apply Arithmetic Mean filter
kernel_size = (3, 3) # 3X3 matrix
denoised_img = cv2.blur(noisy_img, kernel_size)

## display
plt.figure(figsize=(10,10))

plt.subplot(1,3,1)
plt.title("Original img")
plt.imshow(image, cmap='gray')

plt.subplot(1,3,2)
plt.title("Noisy img")
plt.imshow(noisy_img, cmap='gray')

plt.subplot(1,3,3)
plt.title("Denoised img")
plt.imshow(denoised_img, cmap='gray')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()



