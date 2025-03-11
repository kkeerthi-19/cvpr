import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("peacock.png", cv2.IMREAD_GRAYSCALE)
# Logarithmic transformation
def log_transform(img):
  c = 255 / (np.log(1 + np.max(img))) # Scaling constant
  img_log = c * np.log(1 + img)
  return np.uint8(img_log)
# Power-law (gamma) transformation
def power_law_transform(img, gamma=1.5):
  img_norm = img / 255.0 # Normalize image to range [0, 1]
  img_gamma = np.power(img_norm, gamma) * 255 # Apply gamma correction
  return np.uint8(img_gamma)
log_image = log_transform(image)
power_image = power_law_transform(image, gamma=1.5)
titles = ["Original", "Log Transform", "Power-Law (Gamma)"]
images = [image, log_image, power_image]
plt.figure(figsize=(9, 6))
for i in range(len(images)):
  plt.subplot(1, 3, i + 1)
  plt.imshow(images[i], cmap="gray")
  plt.title(titles[i])
  plt.axis("off")
plt.tight_layout()
plt.show()
