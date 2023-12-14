# Transpose the matrix
for row in range(len(matrix)):
    # Iterate over the columns starting from the current row
    for col in range(row, len(matrix)):
        # Swap the current element with its corresponding element across the main diagonal
        temp = matrix[row][col]
        matrix[row][col] = matrix[col][row]
        matrix[col][row] = temp

# Reverse each row
for row in matrix:
    # Reverse the elements in the current row
    row.reverse()
