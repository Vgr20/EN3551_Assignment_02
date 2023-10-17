# find percentage of zeroes
num_zeroes = 0
for x in quantized_dct_blocks:
    for i in range(8):
        for j in range(8):
            if x[i][j] == 0:
                num_zeroes += 1
                
percentage_zeroes = num_zeroes / (quantized_dct_blocks.shape[0] * 64) * 100
print("Percentage of Zeroes : ",percentage_zeroes)

# two dimensional mean square error
error_matrix = image_data - reconstructed_image
mse = np.mean(np.square(error_matrix))
print("Mean Square Error : ",mse)

# calculate the peak signal to noise ratio  
psnr = 20 * np.log10((255) / mse)
print("Peak Signal to Noise Ratio (PSNR) : ",psnr)