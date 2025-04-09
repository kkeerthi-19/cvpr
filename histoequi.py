import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

equalized_img = cv2.equalizeHist(img)

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.hist(img.ravel(), bins=256, range=[0,256], color='blue', alpha=0.7, label='Original Histogram')
plt.title('Original Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.legend()

plt.subplot(2, 2, 3)
plt.imshow(equalized_img, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.hist(equalized_img.ravel(), bins=256, range=[0,256], color='green', alpha=0.7, label='Equalized Histogram')
plt.title('Equalized Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()

cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image', equalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
