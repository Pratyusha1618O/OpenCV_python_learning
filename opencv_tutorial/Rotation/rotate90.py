import cv2
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg",1)

# rotate 90
clock = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
anti_clock = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

plt.figure(figsize=(10, 5))

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1,3,2)
plt.title("Clockwise 90")
plt.imshow(cv2.cvtColor(clock, cv2.COLOR_BGR2RGB))

plt.subplot(1,3,3)
plt.title("Anticlockwise 90")
plt.imshow(cv2.cvtColor(anti_clock, cv2.COLOR_BGR2RGB))

plt.show()

