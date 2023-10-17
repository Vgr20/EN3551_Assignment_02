# inverse quantization
inverse_quantized_dct_blocks = []

for x in quantized_dct_blocks:
    s = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            s[i][j] = x[i][j] * quantization_matrix[i][j]
    inverse_quantized_dct_blocks.append(s)

inverse_quantized_dct_blocks = np.array(inverse_quantized_dct_blocks)

# perform inverse DCT

inverse_dct_blocks = []

for x in inverse_quantized_dct_blocks:
    inverse_dct_blocks.append(scipy.fftpack.idctn(x, norm='ortho'))
inverse_dct_blocks = np.array(inverse_dct_blocks)

inverse_dct_blocks = inverse_dct_blocks + 128
inverse_dct_blocks = inverse_dct_blocks.astype(int)

num_blocks = int(np.sqrt(inverse_dct_blocks.shape[0]))
block_size = inverse_dct_blocks.shape[1]

# Reshape the blocks array
blocks_reshaped = inverse_dct_blocks.reshape((num_blocks, num_blocks, block_size, block_size))

# Initialize an empty image
reconstructed_image = np.zeros((num_blocks * block_size, num_blocks * block_size))

# Reconstruct the image from blocks
for i in range(num_blocks):
    for j in range(num_blocks):
        reconstructed_image[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size] = blocks_reshaped[i, j, :, :]

# Visualize the images
fig,ax = plt.subplots(1,2)
ax[0].imshow(image_data, cmap='gray')
ax[0].set_title('Original Image')
ax[0].axis('off')
ax[1].imshow(reconstructed_image, cmap='gray')
ax[1].set_title('Reconstructed Image')
ax[1].axis('off')
plt.show()