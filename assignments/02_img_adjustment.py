import cv2
import numpy as np
import matplotlib.pyplot as plt

# contrast stretching
def contrast_stretching(image):
    min_val = np.min(image)
    max_val = np.max(image)
    
    stretched_image = (image - min_val) / (max_val - min_val) * 255
    return stretched_image.astype(np.uint8)

# plot the histogram of an image
def plot_histogram(image, title):
    plt.hist(image.ravel(), bins=256, range=(0, 256), color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

# Load the image in grayscale
image = cv2.imread("flower.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to load the image. Please check the file path.")
else:
    # contrast stretching
    contrast_stretched_image = contrast_stretching(image)

    # histogram equalization
    hist_eq_image = cv2.equalizeHist(image)

    #Display
    plt.figure(figsize=(12, 8))

    # Original Image and its Histogram
    plt.subplot(2, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plot_histogram(image, 'Original Image Histogram')

    # Contrast-Stretched Image and its Histogram
    plt.subplot(2, 3, 3)
    plt.imshow(contrast_stretched_image, cmap='gray')
    plt.title('Contrast-Stretched Image')
    plt.axis('off')

    plt.subplot(2, 3, 4)
    plot_histogram(contrast_stretched_image, 'Contrast-Stretched Histogram')

    # Histogram-Equalized Image and its Histogram
    plt.subplot(2, 3, 5)
    plt.imshow(hist_eq_image, cmap='gray')
    plt.title('Histogram-Equalized Image')
    plt.axis('off')

    plt.subplot(2, 3, 6)
    plot_histogram(hist_eq_image, 'Equalized Histogram')

    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()
