#Apply 2 dimensional DCT to each block

dct_blocks = []
for i in range(blocks.shape[0]):
    dct_blocks.append(scipy.fftpack.dctn(blocks[i], norm='ortho'))
dct_blocks = np.array(dct_blocks)

# Quantize the DCT coefficients

quantization_matrix = np.array([[16, 11, 10, 16, 24, 40, 51, 61],[12, 12, 14, 19, 26, 58, 60, 55],[14, 13, 16, 24, 40, 57, 69, 56],[14, 17, 22, 29, 51, 87, 80, 62],[18, 22, 37, 56, 68, 109, 103, 77],[24, 35, 55, 64, 81, 104, 113, 92],[49, 64, 78, 87, 103, 121, 120, 101],[72, 92, 95, 98, 112, 100, 103, 99]])

quality_factor = 5

if quality_factor > 50:
    scale = (100 - quality_factor) / 50
    quantization_matrix = quantization_matrix * scale
else:
    scale = quality_factor / 50
    quantization_matrix = quantization_matrix * scale

quantized_dct_blocks = []


for x in dct_blocks:
    s = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            s[i][j] = round(x[i][j] / quantization_matrix[i][j])
    quantized_dct_blocks.append(s)

quantized_dct_blocks = np.array(quantized_dct_blocks)