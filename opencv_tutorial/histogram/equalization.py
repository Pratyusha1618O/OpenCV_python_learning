import cv2
import matplotlib.pyplot as plt

img = cv2.imread("flower.jpg",0)

#equalization
equ = cv2.equalizeHist(img)

plt.figure(figsize=(10,5))

plt.subplot(2,2,1)
plt.title("Original")
plt.imshow(img, cmap='gray')

plt.subplot(2,2,2)
plt.title("Equalized")
plt.imshow(equ, cmap='gray')

plt.subplot(2,2,3)
plt.title("Histogram of original image")
plt.hist(img.ravel(), 256, [0,256], color='blue')
# plt.xlabel('pixel intensity')
# plt.ylabel('frequency')

plt.subplot(2,2,4)
plt.title("Histogram of equalized image")
plt.hist(equ.ravel(), 256, [0,256], color='blue')

plt.show()
