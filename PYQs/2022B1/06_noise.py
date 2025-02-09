import cv2
import numpy as np

image = cv2.imread("pic.jpg", 0)

## add gaussian noise
mean = 0
sigma = 25
noise = np.random.normal(mean, sigma, image.shape)
noisy_img = image + noise
noisy_img = np.clip(noisy_img, 0, 255)
noisy_img = np.uint8(noisy_img)

cv2.imshow("Noise added", noisy_img)

## remove noise using arithmatic mean filter
ksize=(3,3)
mean_filter = cv2.blur(noisy_img, ksize)

cv2.imshow("Mean filter", mean_filter)


cv2.waitKey(0)
cv2.destroyAllWindows()