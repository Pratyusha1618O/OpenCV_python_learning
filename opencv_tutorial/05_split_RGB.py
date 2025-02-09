import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("pic.jpg")

if img is None:
    print("Image not found")
    exit()

# #extract rgb
B,G,R = cv2.split(img)

# Create blank images for visualization
zero_channel = np.zeros_like(B)

red = cv2.merge([zero_channel, zero_channel, R])
green = cv2.merge([zero_channel, G, zero_channel])
blue = cv2.merge([B, zero_channel, zero_channel])


cv2.imshow("Original image", img)
cv2.imshow("Red channel", red)
cv2.imshow("Green channel", green)
cv2.imshow("Blue channel", blue)



cv2.waitKey(0)
cv2.destroyAllWindows()


# image_array = np.array(img)

# # Extract RGB channels

# red_channel = image_array[:,:,0]    # R component

# green_channel = image_array[:,:,1]  # G component

# blue_channel = image_array[:,:,2]    # B component

# # Display the RGB channels
# plt.figure(figsize=(12, 4))

# plt.subplot(1, 3, 1)
# plt.imshow(red_channel, cmap='Reds')
# plt.title('Red Channel')
# plt.axis('off')

# plt.subplot(1, 3, 2)
# plt.imshow(green_channel, cmap='Greens')
# plt.title('Green Channel')
# plt.axis('off')

# plt.subplot(1, 3, 3)
# plt.imshow(blue_channel, cmap='Blues')
# plt.title('Blue Channel')
# plt.axis('off')

# plt.tight_layout()
# plt.show()