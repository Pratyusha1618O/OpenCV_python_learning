import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("flower.jpg",0)

def  histogram_stretching(img):
    #find maximum and minimum pixel
    min_pixel = np.min(img)
    max_pixel = np.max(img)

    ##stretch the pixel values to the full range (0-255)
    stretched_image = (img - min_pixel)*(255 / (max_pixel - min_pixel))

    #convert into uint8
    stretched_image = np.uint8(stretched_image)

    return stretched_image



if img is None:
    print("Error! image not found, check the file path")
else:
    enhanced_img = histogram_stretching(img)

    # Plotting
    plt.figure(figsize=(10, 10))

    plt.subplot(1,2,1)
    plt.title("Original image")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    plt.subplot(1,2,2)
    plt.title("Enhanced image")
    plt.imshow(cv2.cvtColor(enhanced_img, cv2.COLOR_BGR2RGB))

    plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()