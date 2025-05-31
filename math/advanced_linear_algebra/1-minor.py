def minor(matrix):
    """
    Calculates the minor matrix of a matrix
    
    Args:
        matrix: A list of lists whose minor matrix should be calculated
        
    Returns:
        The minor matrix of the input matrix
        
    Raises:
        TypeError: If matrix is not a list of lists
        ValueError: If matrix is not square or is empty
    """
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is empty
    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")
    
    # Check if all elements are lists
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    
    # Get dimensions
    n = len(matrix)
    
    # Check if matrix is square and non-empty
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")
    
    # Special case: 1x1 matrix
    if n == 1:
        return [[1]]
    
    # Calculate minor matrix
    minor_matrix = []
    
    for i in range(n):
        minor_row = []
        for j in range(n):
            # Create submatrix by removing row i and column j
            submatrix = []
            for row_idx in range(n):
                if row_idx != i:
                    sub_row = []
                    for col_idx in range(n):
                        if col_idx != j:
                            sub_row.append(matrix[row_idx][col_idx])
                    submatrix.append(sub_row)
            
            # Calculate determinant of submatrix
            det = determinant(submatrix)
            minor_row.append(det)
        
        minor_matrix.append(minor_row)
    
    return minor_matrix


def determinant(matrix):
    """
    Helper function to calculate determinant (same as previous implementation)
    """
    # Handle 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]
    
    # Handle 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case for larger matrices
    det = 0
    for col in range(len(matrix)):
        # Create minor matrix
        minor = []
        for row in range(1, len(matrix)):
            minor_row = []
            for c in range(len(matrix)):
                if c != col:
                    minor_row.append(matrix[row][c])
            minor.append(minor_row)
        
        # Calculate cofactor
        cofactor = ((-1) ** col) * matrix[0][col] * determinant(minor)
        det += cofactor
    
    return det
