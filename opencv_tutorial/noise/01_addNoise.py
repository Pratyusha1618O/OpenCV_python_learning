# Adding gaussian noise

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg")

# add noise
mean = 0
sigma = 25 #adjust noise level
noise = np.random.normal(mean, sigma, image.shape)
noisy_img = image + noise
noisy_img = np.clip(noisy_img, 0, 255)
noisy_img = np.uint8(noisy_img)

cv2.imshow("Original image", image)
cv2.imshow("Noisy image", noisy_img)

cv2.imwrite('noisy.jpg', noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
