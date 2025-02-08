import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('flower.jpg', 0)

# apply prewitt operator
prewitt_kernel_x = np.array([[1, 0, -1],
                             [1, 0, -1],
                             [1, 0, -1]])

prewitt_kernel_y = np.array([[1,  1,  1],
                             [0,  0,  0],
                             [-1, -1, -1]])

prewitt_x = cv2.filter2D(image, cv2.CV_64F, prewitt_kernel_x)
prewitt_y = cv2.filter2D(image, cv2.CV_64F, prewitt_kernel_y)
prewitt_edges = cv2.magnitude(prewitt_x, prewitt_y)

# prewitt_edges = np.uint8(prewitt_edges)
# cv2.imshow("prewitt",prewitt_edges)

plt.figure(figsize=(10,10))

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(image, cmap='gray')

plt.subplot(1,2,2)
plt.title("Prewitt operator")
plt.imshow(prewitt_edges, cmap='gray')

plt.show()


