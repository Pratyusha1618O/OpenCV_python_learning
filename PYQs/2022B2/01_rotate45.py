import cv2
import matplotlib.pyplot as plt

image = cv2.imread("sudoku.png")

if image is None:
    print("Image not found")
    exit()

center = (image.shape[1] // 2, image.shape[0] // 2)
rotate_45_clock = cv2.getRotationMatrix2D(center, -45, 1)
rotate_45_anticlock = cv2.getRotationMatrix2D(center, 45, 1)

rotate_45_clock_img = cv2.warpAffine(image, rotate_45_clock, (image.shape[1], image.shape[0]))

rotate_45_anticlock_img = cv2.warpAffine(image, rotate_45_anticlock, (image.shape[1], image.shape[0]))

plt.figure(figsize=(10, 5))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(rotate_45_clock_img, cmap='gray')
plt.title('45 clock')
plt.axis('off')


plt.subplot(2, 3, 3)
plt.imshow(rotate_45_anticlock_img, cmap='gray')
plt.title('45 anticlock')
plt.axis('off')


plt.show()



