import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image and convert to binary
image = cv2.imread('imgg.jpg', cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define kernel (3x3 square)
kernel = np.ones((3, 3), np.uint8)

# Perform morphological operations
erosion = cv2.erode(binary_image, kernel, iterations=1)
dilation = cv2.dilate(binary_image, kernel, iterations=1)
opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(binary_image, cv2.MORPH_GRADIENT, kernel)

# Plot results
titles = ['Original', 'Erosion', 'Dilation', 'Opening', 'Closing', 'Gradient']
images = [binary_image, erosion, dilation, opening, closing, gradient]
plt.figure(figsize=(10, 8))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
