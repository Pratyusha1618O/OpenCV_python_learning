import cv2
import matplotlib.pyplot as plt
img = cv2.imread("pic.jpg")

##conversion from RGB to Gray Scale 
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray scale imaage ", grayscale)

##  conversion from Gray Scale to Binary
_, binary = cv2.threshold(grayscale, 255/2, 255, cv2.THRESH_BINARY)
cv2.imshow("binary image ", binary)

# conversion from RGB to binary 
# conversion of rgb to HSV 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
cv2.imshow("HSV image ", hsv) 

# conversion of HSV to RGB 
hsv_to_rgb= cv2.cvtColor(img, cv2.COLOR_HSV2RGB) 
cv2.imshow("HSV to RGB image ", hsv_to_rgb) 

# conversion of RGB to YCbCr 
YCbCr = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
cv2.imshow("YCbCr image ", YCbCr) 

# conversion of YCbCr to RGB 
ycbcr_to_rgb = cv2.cvtColor(img, cv2.COLOR_YCR_CB2RGB)
cv2.imshow("YCbCr to RGB  image", ycbcr_to_rgb)


# plt.figure(figsize=(15, 10))

# plt.subplot(3, 3, 1)
# plt.imshow(grayscale, cmap='gray')
# plt.title('RGB to Gray')

# plt.subplot(3, 3, 2)
# plt.imshow(binary, cmap='gray')
# plt.title('Gray Scale to Binary')

# plt.subplot(3, 3, 3)
# plt.imshow(hsv)
# plt.title(' rgb to HSV')

# plt.subplot(3, 3, 4)
# plt.imshow(hsv_to_rgb)
# plt.title(' HSV to RGB')

# plt.subplot(3, 3, 5)
# plt.imshow(YCbCr)
# plt.title(' RGB to YCbCr ')

# plt.subplot(3, 3, 6)
# plt.imshow(ycbcr_to_rgb)
# plt.title(' YCbCr to RGB ')

# plt.subplot(3, 3, 7)
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.title('Original')

# # plt.tight_layout()
# plt.subplots_adjust(hspace=0.5)
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
