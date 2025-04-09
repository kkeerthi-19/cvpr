import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale mode
image = cv2.imread('imgg.jpg', cv2.IMREAD_GRAYSCALE)

# Generate a target histogram (this is a simple uniform histogram for example)
target_histogram = np.zeros(256, dtype=np.int32)

# Creating a simple target histogram (uniform distribution)
target_histogram.fill(1)
target_histogram = target_histogram * (image.size // 256)

# Calculate the cumulative distribution function (CDF) of the input image and target histogram
def calculate_cdf(histogram):
    cdf = histogram.cumsum()
    cdf_normalized = cdf * float(histogram.max()) / cdf.max()  # Normalize CDF to match the histogram range
    return cdf_normalized

# Calculate CDF for the source and target histograms
source_histogram, _ = np.histogram(image.flatten(), bins=256, range=[0,256])
target_cdf = calculate_cdf(target_histogram)
source_cdf = calculate_cdf(source_histogram)

# Map the pixel values based on the CDFs
mapping = np.interp(source_cdf, target_cdf, np.arange(256))

# Apply the mapping to the image
mapped_image = mapping[image]

# Convert mapped image to uint8 type
mapped_image = np.uint8(mapped_image)

# Plot the original image, mapped image, and histograms
plt.figure(figsize=(12, 6))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Mapped image
plt.subplot(2, 2, 2)
plt.imshow(mapped_image, cmap='gray')
plt.title('Mapped Image')
plt.axis('off')

# Plot histograms

# Original image histogram
plt.subplot(2, 2, 3)
plt.hist(image.ravel(), bins=256, range=(0, 256), color='black')
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Mapped image histogram
plt.subplot(2, 2, 4)
plt.hist(mapped_image.ravel(), bins=256, range=(0, 256), color='black')
plt.title('Histogram of Mapped Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Show the plots
plt.tight_layout()
plt.show()

# Optionally, save the mapped image
cv2.imwrite('mapped_image.jpg', mapped_image)
