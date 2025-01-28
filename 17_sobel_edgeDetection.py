import cv2
import matplotlib.pyplot as plt

# Load and preprocess the image
image = cv2.imread('krishna.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hgt, wdt, _ = image.shape

# Sobel Edges
x_sobel = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
y_sobel = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

# Plot the results
plt.figure(figsize=(20, 20))

# Original Image
plt.subplot(3, 2, 1)
plt.title("Original")
plt.imshow(image)

# Sobel X
plt.subplot(3, 2, 2)
plt.title("Sobel X")
plt.imshow(x_sobel, cmap='gray')

# Sobel Y
plt.subplot(3, 2, 3)
plt.title("Sobel Y")
plt.imshow(y_sobel, cmap='gray')

# Combine X and Y Sobel Edges
sobel_or = cv2.bitwise_or(x_sobel.astype('uint8'), y_sobel.astype('uint8'))
plt.subplot(3, 2, 4)
plt.title("Sobel OR")
plt.imshow(sobel_or, cmap='gray')

# Show the plots
plt.show()
