import cv2
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow("Gaussian", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
