import numpy as np
import matplotlib.pyplot as plt
import scipy
import sympy

# Load the .mat file into a dictionary
mat_data = scipy.io.loadmat('SampleImages/camera256.mat')

# Extract the image data from the dictionary
image_data = mat_data['camera256']

image_data = image_data.astype(np.int16)

# Display the image using Matplotlib
plt.imshow(image_data, cmap='gray')
plt.axis('on')
plt.show()

# Separate image into 8x8 blocks
block_size = 8
blocks = []
for i in range(0, image_data.shape[0], block_size):
    for j in range(0, image_data.shape[1], block_size):
        blocks.append(image_data[i:i+block_size, j:j+block_size])

# Convert blocks to numpy array
blocks = np.array(blocks)
blocks = blocks - 128
