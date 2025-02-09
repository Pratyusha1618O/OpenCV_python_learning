import cv2
import numpy as np

# Load the two images
img1 = cv2.imread("pic.jpg")
img2 = cv2.imread("sudoku.png")

# Resize images to the same size if needed
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# average
avg = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.imshow("Average img", avg)

cv2.waitKey(0)
cv2.destroyAllWindows()
