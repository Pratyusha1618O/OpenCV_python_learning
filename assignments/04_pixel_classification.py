# Classify pixels and work with RGB and grayscale images. 
# Problem: 
# 1. Load an RGB image and convert it to a grayscale image using OpenCV. 
# 2. Perform pixel classification by thresholding (e.g., segment bright areas of the image). 
# 3. Highlight the classified regions in the original RGB image using a different color. 
# 4. Display the original RGB image, grayscale image, and the classified image.

import cv2 
import matplotlib.pyplot as plt

img = cv2.imread("flower1.jpeg",100)

## converting into grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Perform pixel classification by thresholding
threshold_value, classified_img = cv2.threshold(gray_img, 180, 255, cv2.THRESH_BINARY)

## Highlight the classified regions in the original RGB image using a different color. 
highlighted_img = img.copy()  
highlighted_img[classified_img == 255] = [0, 0, 255]  # Color bright areas in red

## Display the original RGB image, grayscale image, and the classified image.
cv2.imshow("original", img)
cv2.imshow("Grayscale image", gray_img)
cv2.imshow("Highlighted image", highlighted_img)

cv2.waitKey(0)
