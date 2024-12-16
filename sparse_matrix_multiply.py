from collections import defaultdict

def multiply_sparse_matrices(A, B):
    """
    Multiplies two sparse matrices A and B.

    Parameters:
        A (list of lists): The first matrix, of size m x n.
        B (list of lists): The second matrix, of size n x p.
    
    Returns:
        list of lists: The resultant matrix after multiplication, of size m x p.

    Raises:
        ValueError: If the number of columns in A does not equal the number of rows in B.
    """
    
    # Validate matrix dimensions to ensure A's columns match B's rows
    if len(A[0]) != len(B):
        raise ValueError("A's column number must be equal to B's row number")

    # Convert B into a column-centric sparse representation
    # This optimizes lookup during multiplication by storing only non-zero values in each column of B
    sparse_B = defaultdict(list)
    for col in range(len(B[0])):  # Iterate over columns of B
        for row in range(len(B)):  # Iterate over rows of B
            if B[row][col] != 0:  # Store only non-zero elements
                sparse_B[col].append((row, B[row][col]))

    # Initialize the result matrix with zeros, of size m x p
    result = [[0] * len(B[0]) for _ in range(len(A))]

    # Perform sparse matrix multiplication
    # Iterate over each element in A
    for i in range(len(A)):  # For each row in A
        for j in range(len(A[0])):  # For each column in A
            if A[i][j] != 0:  # Process only non-zero elements in A
                # Multiply A's non-zero element with corresponding non-zero elements in B
                for row_idx, value in sparse_B[j]:  # Sparse representation of column j in B
                    result[i][row_idx] += A[i][j] * value  # Accumulate the product in the result matrix

    return result

# Compute the result of A * B
result = multiply_sparse_matrices(A, B)

# Print the result matrix row by row
for row in result:
    print(row)
