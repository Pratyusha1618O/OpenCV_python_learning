## Add Salt and Pepper Noise

import cv2
import random

image = cv2.imread("flower.jpg",0)

noisy_img = image.copy()

salt_prob = 0.02
pepper_prob = 0.02

total_pixel = image.size 

#Add salt
salt = int(total_pixel * salt_prob)
for i in range(salt):
    i = random.randint(0, image.shape[0]-1) #random row
    j = random.randint(0, image.shape[1]-1) #random column
    noisy_img[i, j] = 255 # set pixel to white

# Add pepper
pepper = int(total_pixel * pepper_prob)
for i in range(pepper):
    i = random.randint(0, image.shape[0]-1)
    j = random.randint(0, image.shape[1]-1)
    noisy_img[i,j] = 0 # set pixel to black

cv2.imshow("Original image", image)
cv2.imshow("Salt pepper noise added", noisy_img)

cv2.waitKey(0)
cv2.destroyAllWindows()