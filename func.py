import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('bird.jpg', cv2.IMREAD_GRAYSCALE)
# Function for Brightness Adjustment
def adjust_brightness(image, brightness_value):
  brightness_adjusted = cv2.add(image, brightness_value)
  return brightness_adjusted
# Function for Contrast Adjustment
def adjust_contrast(image, contrast_value):
  contrast_adjusted = cv2.convertScaleAbs(image, alpha=contrast_value, beta=0)
  return contrast_adjusted
# Display the images for comparison
def display_images(images, titles):
  plt.figure(figsize=(10, 10))
  for i, (img, title) in enumerate(zip(images, titles)):
    plt.subplot(2, 3, i+1)
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
  plt.tight_layout()
  plt.show()
brightness_adjusted = adjust_brightness(image, 50)
contrast_adjusted = adjust_contrast(image, 1.5)
images = [image, brightness_adjusted, contrast_adjusted]
titles = ['Original','Brightness Adjusted', 'Contrast Adjusted']
display_images(images, titles)
