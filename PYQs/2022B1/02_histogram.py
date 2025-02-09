import cv2
import matplotlib.pyplot as plt

img = cv2.imread("pic.jpg",0)

if img is None:
    print("Image not found")
    exit()

# hist = cv2.calcHist([img], [0], None, [256], [0,256])
# plt.plot(hist)

plt.figure(figsize=(15,5))

plt.subplot(1,2,1)
plt.title("Image")
plt.imshow(img, cmap='gray')

plt.subplot(1,2,2)
plt.title("Histogram")
plt.hist(img.ravel(), 256, (0, 256), color='blue')
plt.xlabel("Pixel intensity")
plt.ylabel("Frequency")

plt.show()