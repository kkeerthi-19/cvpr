import cv2
import numpy as np
import matplotlib.pyplot as plt
image1_path = "src.jpg"
image2_path = "ref.jpg"
image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
image1 = cv2.resize(image1, (300, 300))
image2 = cv2.resize(image2, (300, 300))
image_add = cv2.add(image1, image2) # Addition
image_subtract = cv2.subtract(image1, image2) # Subtraction
image_multiply = cv2.multiply(image1, image2) # Multiplication
image_divide = cv2.divide(image1, image2) # Division
titles = ["Image 1", "Image 2", "Addition", "Subtraction", "Multiplication", "Division"]
images = [image1, image2, image_add, image_subtract, image_multiply, image_divide]
plt.figure(figsize=(10, 8))
for i in range(len(images)):
 plt.subplot(2, 3, i + 1)
 plt.imshow(images[i], cmap="gray")
 plt.title(titles[i])
 plt.axis("off")
plt.tight_layout()
plt.show()
