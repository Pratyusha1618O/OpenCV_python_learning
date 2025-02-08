import cv2

image = cv2.imread("noisy.jpg")

## Apply arithmetic mean filter
kernel_size = (3, 3)
mean_filter = cv2.blur(image, kernel_size)
# filtered_img = cv2.boxFilter(image, -1, (7,7), normalize=True)

cv2.imshow("Original image", image)
cv2.imshow("Mean filtered", mean_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()