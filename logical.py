import cv2
import numpy as np
import matplotlib.pyplot as plt
# binary images
image1 = np.zeros((300, 300), dtype=np.uint8)
image2 = np.zeros((300, 300), dtype=np.uint8)
cv2.rectangle(image1, (50, 50), (250, 250), 255, -1)
cv2.circle(image2, (150, 150), 100, 255, -1)
and_image = cv2.bitwise_and(image1, image2) # AND operation
or_image = cv2.bitwise_or(image1, image2) # OR operation
xor_image = cv2.bitwise_xor(image1, image2) # XOR operation
not_image1 = cv2.bitwise_not(image1) # NOT operation on image1
not_image2 = cv2.bitwise_not(image2) # NOT operation on image2
titles = [
 "Image 1", "Image 2", "AND Operation", "OR Operation",
 "XOR Operation", "NOT Operation (Image 1)", "NOT Operation (Image 2)"
]
images = [image1, image2, and_image, or_image, xor_image, not_image1, not_image2]
plt.figure(figsize=(12, 10))
for i in range(len(images)):
 plt.subplot(3, 3, i + 1)
 plt.imshow(images[i], cmap="gray")
 plt.title(titles[i])
 plt.axis("off")
plt.tight_layout()
plt.show()
