#  Write a program to perform image enhancement using Piecewise Linear Transformation. Then
# compare the enhanced image with original image using image subtraction. The original input image
# using image should be greyscale. Display the output images.

import cv2
import numpy as np

image = cv2.imread("pic.jpg",0)

def piecewise_linear_transform(pixel):
    if pixel < 100:
        return pixel * 0.5
    elif pixel < 200:
        return 0.8 * pixel + 50
    else:
        return min(255, 1.2 * pixel)
    
vectorized_transform = np.vectorize(piecewise_linear_transform)
enhanced_img = np.uint8(vectorized_transform(image))

# subtract
sub = cv2.absdiff(enhanced_img, image)

cv2.imshow("Original Image", image)
cv2.imshow("Enhanced Image", enhanced_img)
cv2.imshow("Subtracted Image (Difference)", sub)

cv2.waitKey(0)
cv2.destroyAllWindows()