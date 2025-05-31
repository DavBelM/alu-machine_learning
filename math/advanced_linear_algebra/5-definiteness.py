#!/usr/bin/env python3

import numpy as np


def definiteness(matrix):
    """
    Calculates the definiteness of a matrix
    
    Args:
        matrix: A numpy.ndarray of shape (n, n) whose definiteness should be calculated
        
    Returns:
        String indicating the definiteness of the matrix:
        - "Positive definite"
        - "Positive semi-definite" 
        - "Negative semi-definite"
        - "Negative definite"
        - "Indefinite"
        - None if matrix is not valid
        
    Raises:
        TypeError: If matrix is not a numpy.ndarray
    """
    # Check if matrix is a numpy array
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    
    # Check if matrix is empty
    if matrix.size == 0:
        return None
    
    # Check if matrix is 2D
    if matrix.ndim != 2:
        return None
    
    # Check if matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        return None
    
    # Check if matrix is symmetric (required for definiteness)
    if not np.allclose(matrix, matrix.T):
        return None
    
    # Calculate eigenvalues
    try:
        eigenvalues = np.linalg.eigvals(matrix)
    except np.linalg.LinAlgError:
        return None
    
    # Remove very small values (numerical errors)
    eigenvalues = eigenvalues.real
    tolerance = 1e-8
    
    # Count positive, negative, and zero eigenvalues
    positive_count = np.sum(eigenvalues > tolerance)
    negative_count = np.sum(eigenvalues < -tolerance)
    zero_count = np.sum(np.abs(eigenvalues) <= tolerance)
    
    n = len(eigenvalues)
    
    # Determine definiteness based on eigenvalues
    if positive_count == n:
        return "Positive definite"
    elif positive_count + zero_count == n and zero_count > 0:
        return "Positive semi-definite"
    elif negative_count == n:
        return "Negative definite"
    elif negative_count + zero_count == n and zero_count > 0:
        return "Negative semi-definite"
    elif positive_count > 0 and negative_count > 0:
        return "Indefinite"
    else:
        return None
