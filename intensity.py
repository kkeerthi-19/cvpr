import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
# Load a grayscale image 
image = cv2.imread('img7.jpg', cv2.IMREAD_COLOR_RGB)  # Make sure to read it as grayscale 
 
# Define the intensity range to slice 
lower_threshold = 50  # Lower intensity value 
upper_threshold = 100  # Upper intensity value 
 
# Create an output image where we will store the sliced results 
output_image = np.zeros_like(image) 
# Apply intensity level slicing 
output_image[(image >= lower_threshold) & (image <= upper_threshold)] = 255 
 
# Display the original and sliced images side by side for comparison 
plt.figure(figsize=(10, 5)) 
 
# Plot original image (already in grayscale) 
plt.subplot(1, 2, 1) 
plt.title('Original Image') 
plt.imshow(image) 
plt.axis('off') 
 
# Plot the intensity sliced image 
plt.subplot(1, 2, 2) 
plt.title(f'Intensity Sliced ({lower_threshold}-{upper_threshold})') 
plt.imshow(output_image) 
plt.axis('off') 
plt.show() 
