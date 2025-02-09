import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread("pic.jpg",0)

kx = np.array([[1, 0],
               [0,-1]])

ky = np.array([[0, 1],
               [-1, 0]])

edge_x = cv2.filter2D(img, -1, kx)
edge_y = cv2.filter2D(img, -1, ky)

edges = cv2.add(edge_x, edge_y)

cv2.imshow("Roberts Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()