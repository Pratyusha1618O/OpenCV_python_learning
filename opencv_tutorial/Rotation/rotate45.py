import cv2
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg")

r = image.shape[0]
c = image.shape[1]
center = (c//2, r//2)

# clock wise
rotation_matrix_clock = cv2.getRotationMatrix2D(center, -45, 1)
clock_img = cv2.warpAffine(image, rotation_matrix_clock, (c, r))

# Anti clock wise
rotation_matrix_anticlock = cv2.getRotationMatrix2D(center, 45, 1)
anticlock_img = cv2.warpAffine(image, rotation_matrix_anticlock, (c, r))


plt.figure(figsize=(10, 5))

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1,3,2)
plt.title("Clockwise 45")
plt.imshow(cv2.cvtColor(clock_img, cv2.COLOR_BGR2RGB))

plt.subplot(1,3,3)
plt.title("Anticlockwise 45")
plt.imshow(cv2.cvtColor(anticlock_img, cv2.COLOR_BGR2RGB))

plt.show()

