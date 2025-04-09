import numpy as np
import cv2
import matplotlib.pyplot as plt

# Function to create a Gaussian kernel
def gaussian_kernel(size, sigma):
    """Generates a Gaussian kernel."""
    kernel = np.fromfunction(
        lambda x, y: (1 / (2 * np.pi * sigma**2)) * 
                     np.exp(-((x - (size - 1) / 2) ** 2 + (y - (size - 1) / 2) ** 2) / (2 * sigma**2)),
        (size, size)
    )
    return kernel / np.sum(kernel)

# Function to apply Gaussian filter to an image using a kernel
def apply_gaussian_filter(image, kernel):
    """Applies a Gaussian filter to an image using element-wise multiplication."""
    kernel_size = kernel.shape[0]
    padded_image = np.pad(image, pad_width=((kernel_size // 2, kernel_size // 2), (kernel_size // 2, kernel_size // 2)), mode='constant', constant_values=0)
    
    output_image = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i + kernel_size, j:j + kernel_size]
            output_image[i, j] = np.sum(region * kernel)  # Element-wise multiplication and summation
    return output_image

# Load the image in grayscale
image = cv2.imread('bird.jpg', cv2.IMREAD_GRAYSCALE)

# Create the Gaussian kernel
kernel_size = 5  # Size of the kernel (must be odd)
sigma = 1         # Standard deviation for the Gaussian function
kernel = gaussian_kernel(kernel_size, sigma)

# Apply the Gaussian filter
filtered_image = apply_gaussian_filter(image, kernel)

# Display the original and filtered images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Filtered Image with Gaussian Kernel')
plt.imshow(filtered_image, cmap='gray')
plt.axis('off')

plt.show()

# Optionally, save the filtered image
cv2.imwrite('filtered_image_gaussian.jpg', filtered_image)
