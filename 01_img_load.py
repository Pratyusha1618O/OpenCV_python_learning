import cv2
print(cv2.__version__)

#coloured image
img = cv2.imread('jjk.jpg',0)
img = cv2.imread('jjk.jpg',1)

resize_img = cv2.resize(img,(600,400))
cv2.imshow("rgb img",resize_img)

#Black n white (Gray scale)
# img1 = cv2.imread("jjk.jpg",0)
cv2.waitKey(0)
cv2.destroyAllWindows()