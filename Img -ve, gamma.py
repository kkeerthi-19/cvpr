import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image in grayscale
img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Image Negative: s = 255 - r
negative_img = 255 - img

# Gamma Transformation: s = c * r^gamma
gamma = 2.0       # Try values like 0.5, 1.0, 2.0
c = 1             # Constant multiplier
gamma_img = np.array(255 * (img / 255) ** gamma, dtype='uint8')

# Display results
titles = ['Original Image', 'Negative Image', f'Gamma = {gamma}']
images = [img, negative_img, gamma_img]

plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
