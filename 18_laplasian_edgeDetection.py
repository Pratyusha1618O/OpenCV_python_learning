import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('krishna.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for display

# Laplacian Edge Detection
laplacian = cv2.Laplacian(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY), cv2.CV_64F)

# Canny Edge Detection
canny = cv2.Canny(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY), 50, 120)

# Plotting
plt.figure(figsize=(10, 10))

# Laplacian Edge Detection Result
plt.subplot(1, 2, 1)
plt.title("Laplacian")
plt.imshow(laplacian, cmap='gray')

# Canny Edge Detection Result
plt.subplot(1, 2, 2)
plt.title("Canny")
plt.imshow(canny, cmap='gray')

# Show the results
plt.show()
