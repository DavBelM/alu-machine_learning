#!/usr/bin/env python3

def determinant(matrix):
    """
    Calculates the determinant of a matrix
    
    Args:
        matrix: A list of lists whose determinant should be calculated
        
    Returns:
        The determinant of the matrix
        
    Raises:
        TypeError: If matrix is not a list of lists
        ValueError: If matrix is not square
    """
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    
    # Handle empty matrix case
    if len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    
    # Handle 0x0 matrix case [[]]
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 1
    
    # Check if all elements are lists
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    
    # Get dimensions
    n = len(matrix)
    
    # Check if matrix is square
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a square matrix")
    
    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0][0]
    
    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case: use cofactor expansion along first row
    det = 0
    for col in range(n):
        # Create minor matrix by removing first row and current column
        minor = []
        for row in range(1, n):
            minor_row = []
            for c in range(n):
                if c != col:
                    minor_row.append(matrix[row][c])
            minor.append(minor_row)
        
        # Calculate cofactor: (-1)^(0+col) * matrix[0][col] * det(minor)
        cofactor = ((-1) ** col) * matrix[0][col] * determinant(minor)
        det += cofactor
    
    return det
