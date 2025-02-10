import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("sudoku.png",0)

#apply sobel operator
sobel_x = cv2.Sobel(image, cv2.CV_8U, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_8U, 0, 1, ksize=3)
sobel_edges = sobel_x + sobel_y

# sobel_edges = np.uint8(np.abs(sobel_edges))
# edges_x = np.uint8(np.abs(sobel_x))
# edges_y = np.uint8(np.abs(sobel_y))

cv2.imshow("sobel", sobel_edges)
cv2.imshow("sobel x", sobel_x)
cv2.imshow("sobel y", sobel_y)


# plt.figure(figsize=(10,10))

# plt.subplot(2,2,1)
# plt.title("Original Image")
# plt.imshow(image, cmap='gray')

# plt.subplot(2,2,2)
# plt.title("Sobel detected Image")
# plt.imshow(sobel_edges, cmap='gray')

# plt.subplot(2,2,3)
# plt.title("Sobel x detected Image")
# plt.imshow(sobel_x, cmap='gray')


# plt.subplot(2,2,4)
# plt.title("Sobel y detected Image")
# plt.imshow(sobel_y, cmap='gray')


plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()