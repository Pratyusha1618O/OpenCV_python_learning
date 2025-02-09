import cv2
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg")

# rotate 45
center = (image.shape[1] // 2, image.shape[0] // 2)
rotation_45_clock = cv2.getRotationMatrix2D(center, -45, 1) #rotate -45 clockwise
rotation_45_anticlock = cv2.getRotationMatrix2D(center, 45, 1) #rotate 45 clockwise

rotated_img_clock = cv2.warpAffine(image, rotation_45_clock, (image.shape[1], image.shape[0]))

rotate_img_anticlock = cv2.warpAffine(image, rotation_45_anticlock, (image.shape[1], image.shape[0]))


plt.figure(figsize=(10, 5))

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1,3,2)
plt.title("Clockwise 90")
plt.imshow(cv2.cvtColor(rotated_img_clock, cv2.COLOR_BGR2RGB))

plt.subplot(1,3,3)
plt.title("Anticlockwise 90")
plt.imshow(cv2.cvtColor(rotate_img_anticlock, cv2.COLOR_BGR2RGB))

plt.show()

