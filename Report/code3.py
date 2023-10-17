# Coding the DC coefficients

dc_coefficients = []
for x in quantized_dct_blocks:
    dc_coefficients.append(x[0][0])

# differential pulse code modulation for DC coefficients

dpcm_dc_coefficients = []
dpcm_dc_coefficients.append(dc_coefficients[0])
for i in range(1, len(dc_coefficients)):
    dpcm_dc_coefficients.append(dc_coefficients[i] - dc_coefficients[i-1])

# run,level modulation for AC pairs

run_level_pairs_blocks = []

for x in quantized_dct_blocks:
    run = 0
    level = 0
    run_level_pairs = []
    for i in range(1, 8):
        for j in range(1, 8):
            if x[i][j] != 0:
                run_level_pairs.append((run, level))
                run = 0
                level = x[i][j]
            else:
                run += 1
                
    run_level_pairs_blocks.append(run_level_pairs)

    # Entropy coding for run-level pairs

entropy_coded_blocks = []

for x in run_level_pairs_blocks:
    entropy_coded_block = []
    for i in range(len(x)):
        if i == 0:
            entropy_coded_block.append((x[i][0], x[i][1]))
        else:
            if x[i][0] == 0 and x[i][1] == 0:
                entropy_coded_block.append((15, 0))
            else:
                entropy_coded_block.append((x[i][0], x[i][1]))
    entropy_coded_blocks.append(entropy_coded_block)

