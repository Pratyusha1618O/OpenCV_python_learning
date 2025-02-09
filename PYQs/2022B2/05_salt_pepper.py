import cv2
import numpy as np
import random

image = cv2.imread("pic.jpg")

noisy_img = image.copy()

salt_prob = 0.02
pepper_prob = 0.02

total_pixel = image.size

#add salt
salt = int(total_pixel * salt_prob)
for i in range(salt):
    i = random.randint(0, image.shape[0] - 1)
    j = random.randint(0, image.shape[1] - 1)
    noisy_img[i][j] = 255

#add pepper
pepper = int(total_pixel * pepper_prob)
for i in range(pepper):
    i = random.randint(0, image.shape[0] - 1)
    j = random.randint(0, image.shape[1] - 1)
    noisy_img[i][j] = 0

cv2.imshow("Noisy img", noisy_img)

# median blur
median = cv2.medianBlur(noisy_img, 5)
cv2.imshow("Blured img", median)


cv2.waitKey(0)
cv2.destroyAllWindows()
