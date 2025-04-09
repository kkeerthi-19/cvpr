import cv2
import numpy as np

image = cv2.imread("img0.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Could not load image. Check the file path.")
    exit()

negative_image = 255 - image

c = 255 / (np.log(1 + np.max(image)))  
log_image = c * np.log(1 + image.astype(np.float32))
log_image = np.uint8(log_image)
gamma=2.2
gamma_corrected = np.array(255 * (image / 255) ** gamma, dtype=np.uint8)

cv2.imshow("Original Image", image)
cv2.imshow("Negative Image", negative_image)
cv2.imshow("Log Transformed Image", log_image)
cv2.imshow("Gamma Corrected Image", gamma_corrected)

cv2.waitKey(0)
cv2.destroyAllWindows()