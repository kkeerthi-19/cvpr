import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
 
# Load a grayscale image 
image = cv2.imread('img7.jpg', cv2.IMREAD_COLOR_RGB) 
 
# Function to perform bit-level slicing 
def bit_level_slicing(image, bit_position): 
    # Create a mask for the specific bit position (bit_position: 0 to 7) 
    mask = 1 << bit_position 
 
    # Apply the mask and shift right to isolate the desired bit 
    sliced_image = (image & mask) >> bit_position 
 
    # Scale to 255 (white) for visibility in display 
    sliced_image = sliced_image * 255 
 
    return sliced_image 
 
# Perform bit-level slicing for each bit from 0 to 7 
bit_slices = [] 
for bit in range(8): 
    sliced_img = bit_level_slicing(image, bit) 
    bit_slices.append(sliced_img) 
 
# Display the original image and bit-level slices 
plt.figure(figsize=(12, 8)) 
 
# Display the original image 
plt.subplot(3, 3, 1) 
plt.title('Original Image') 
plt.imshow(image) 
plt.axis('off') 
 
# Display the bit-level slices 
for i in range(8): 
    plt.subplot(3, 3, i + 2) 
    plt.title(f'Bit {i}') 
    plt.imshow(bit_slices[i])
    plt.axis('off')
plt.show()
