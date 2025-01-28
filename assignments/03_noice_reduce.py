# # Understand and apply noise smoothing and sharpening techniques. 
# # Problem: 
# # 1. Load a noisy image or add noise to an image using a Gaussian noise generator. 
# # 2. Apply smoothing techniques using: 
# # o Gaussian blur. 
# # o Median blur. 
# # 3. Sharpen the image using a Laplacian filter. 
# # 4. Compare and display the results of smoothing and sharpening techniques.

import cv2
import numpy as np
import matplotlib.pyplot as plt


#loading noisy image
img = cv2.imread("flower2.jpg")

gaussian_blur = cv2.GaussianBlur(img, (7,7), 0) 
median_blur = cv2.medianBlur(img,5)

laplacian = cv2.Laplacian(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), cv2.CV_64F)

# Plotting
plt.figure(figsize=(10, 10))

# Displaying the noisy and processed images
plt.subplot(2,2,1)
plt.title("Noisy Image")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(2,2,2)
plt.title("Gaussian Blur")
plt.imshow(cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2RGB))

plt.subplot(2,2,3)
plt.title("Median Blur")
plt.imshow(cv2.cvtColor(median_blur, cv2.COLOR_BGR2RGB))

# Laplacian Edge Detection Result
plt.subplot(2,2,4)
plt.title("Laplacian")
plt.imshow(laplacian, cmap='gray')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

 