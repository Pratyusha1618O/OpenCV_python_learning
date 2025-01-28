import cv2 
img = cv2.imread("krishna.jpg") 
edge_img = cv2.Canny(img,100,200) 
cv2.imshow("Detected Edges", edge_img) 
cv2.waitKey(0)