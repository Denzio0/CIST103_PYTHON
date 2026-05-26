#MARC RODEN D. FAMERO
#DATA STRUCTURES AND ALGORITHM - DSA (CIST103)
#LABORATORY EXERCISE — Problem Number 1

    # Simulated array storage address calculation
    # Dimensions of array (2D)
rows = 3
cols = 4

    # Element size (word size in bytes)
word_size = 4

    # Base address (assumed)
base_address = 1000

    # Target element indices
i = 1   # row index
j = 2   # column index

    # Row-major address calculation
row_major_address = base_address + word_size * (i * cols + j)

    # Column-major address calculation
column_major_address = base_address + word_size * (j * rows + i)

print("Base Address:", base_address)
print("Word Size:", word_size, "bytes")

print("\nRow-Major Order Address:")
print("Address of element [", i, "][", j, "] =", row_major_address)

print("\nColumn-Major Order Address:")
print("Address of element [", i, "][", j, "] =", column_major_address)
