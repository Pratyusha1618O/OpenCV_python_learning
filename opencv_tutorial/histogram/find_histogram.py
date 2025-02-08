import cv2
from matplotlib import pyplot as plt

img = cv2.imread('flower.jpg',0)

if img is None:
    print("Image not found")
    exit()

cv2.imshow("Image", img)

# hist = cv2.calcHist([img], [0], None, [256], [0,256])

plt.hist(img.ravel(), 256, [0, 256], color='blue')

# plt.plot(hist)
plt.show()