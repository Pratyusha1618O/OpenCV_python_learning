import cv2
image = cv2.imread("pic.jpg")

if image is None:
    print("Error: Could not read the image.")
    exit()


# Remove colors by setting channels to 0
no_red = image.copy()
no_red[:, :, 2] = 0  # Remove Red

no_green = image.copy()
no_green[:, :, 1] = 0  # Remove Green

no_blue = image.copy()
no_blue[:, :, 0] = 0  # Remove Blue


# Display images
# for title, img in zip(["Original", "No Red", "No Blue", "No Green"], [image, no_red, no_blue, no_green]):
#     cv2.imshow(title, img)
cv2.imshow("No red", no_red)
cv2.imshow("No green", no_green)
cv2.imshow("No blue", no_blue)

cv2.waitKey(0)
cv2.destroyAllWindows()
