import cv2
import numpy as np

image = cv2.imread("pic.jpg", 0)
low_sampled = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2))

cv2.imshow("Original", image)
cv2.imshow("Low Sampled", low_sampled)

quantized = (image // 64) * 64  # Reduces intensity levels to 4 (0, 64, 128, 192)
cv2.imshow("Quantized", quantized)



cv2.waitKey(0)
cv2.destroyAllWindows()
