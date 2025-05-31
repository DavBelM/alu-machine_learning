# Advanced Linear Algebra

This directory contains implementations of fundamental advanced linear algebra operations using pure Python (no NumPy dependencies except where specified).

## Overview

The project implements core matrix operations from scratch, including determinant calculation, matrix decomposition, and definiteness analysis. These implementations provide a deep understanding of the mathematical concepts behind linear algebra operations.

## Files and Functions

### 0. Determinant (`0-determinant.py`)

```python
def determinant(matrix):
```

Calculates the determinant of a square matrix using recursive cofactor expansion.

**Features:**

- Handles matrices of any size (1×1, 2×2, n×n)
- Special case handling for 0×0 matrix (`[[]]` returns 1)
- Recursive implementation using cofactor expansion along the first row
- Input validation for matrix format and square constraint

**Example:**

```python
mat = [[1, 2], [3, 4]]
print(determinant(mat))  # Output: -2
```

### 1. Minor Matrix (`1-minor.py`)

```python
def minor(matrix):
```

Calculates the minor matrix by computing determinants of all possible submatrices.

**Features:**

- Creates (n-1)×(n-1) submatrices by removing each row and column
- Calculates determinant for each submatrix
- Returns matrix of the same size with minor values

**Example:**

```python
mat = [[1, 2], [3, 4]]
print(minor(mat))  # Output: [[4, 3], [2, 1]]
```

### 2. Cofactor Matrix (`2-cofactor.py`)

```python
def cofactor(matrix):
```

Calculates the cofactor matrix by applying alternating signs to the minor matrix.

**Features:**

- Uses the minor matrix as base
- Applies sign pattern: `(-1)^(i+j)` for position (i,j)
- Creates checkerboard pattern of positive/negative signs

**Example:**

```python
mat = [[1, 2], [3, 4]]
print(cofactor(mat))  # Output: [[4, -3], [-2, 1]]
```

### 3. Adjugate Matrix (`3-adjugate.py`)

```python
def adjugate(matrix):
```

Calculates the adjugate (adjoint) matrix as the transpose of the cofactor matrix.

**Features:**

- Computes cofactor matrix first
- Transposes the cofactor matrix: `adj[i][j] = cof[j][i]`
- Essential for matrix inversion: `A^(-1) = (1/det(A)) × adj(A)`

**Example:**

```python
mat = [[1, 2], [3, 4]]
print(adjugate(mat))  # Output: [[4, -2], [-3, 1]]
```

### 4. Matrix Inverse (`4-inverse.py`)

```python
def inverse(matrix):
```

Calculates the inverse of a matrix using the adjugate method.

**Features:**

- Returns `None` for singular matrices (determinant = 0)
- Uses formula: `A^(-1) = (1/det(A)) × adjugate(A)`
- Returns floating-point results
- Comprehensive singularity checking

**Example:**

```python
mat = [[1, 2], [3, 4]]
print(inverse(mat))  # Output: [[-2.0, 1.0], [1.5, -0.5]]
```

### 5. Matrix Definiteness (`5-definiteness.py`)

```python
def definiteness(matrix):
```

Determines the definiteness of a symmetric matrix using eigenvalue analysis.

**Features:**

- Requires NumPy for eigenvalue computation
- Checks matrix symmetry as prerequisite
- Classifies based on eigenvalue signs:
  - **Positive definite**: All eigenvalues > 0
  - **Positive semi-definite**: All eigenvalues ≥ 0, at least one = 0
  - **Negative definite**: All eigenvalues < 0
  - **Negative semi-definite**: All eigenvalues ≤ 0, at least one = 0
  - **Indefinite**: Both positive and negative eigenvalues

**Example:**

```python
import numpy as np
mat = np.array([[2, 1], [1, 2]])
print(definiteness(mat))  # Output: "Positive definite"
```

## Mathematical Concepts

### Determinant

The determinant is a scalar value that provides important information about a matrix:

- Non-zero determinant indicates invertible matrix
- Zero determinant indicates singular (non-invertible) matrix
- Used in solving systems of linear equations (Cramer's rule)

### Minor and Cofactor

- **Minor M_ij**: Determinant of submatrix obtained by removing row i and column j
- **Cofactor C_ij**: Minor with alternating sign: `C_ij = (-1)^(i+j) × M_ij`
- Form the basis for determinant calculation and matrix inversion

### Adjugate Matrix

- Transpose of the cofactor matrix
- Key component in matrix inversion formula
- Properties: `A × adj(A) = det(A) × I`

### Matrix Inverse

- Exists only for non-singular (invertible) matrices
- Satisfies: `A × A^(-1) = A^(-1) × A = I`
- Applications: solving linear systems, transformations

### Matrix Definiteness

Important for optimization and stability analysis:

- **Positive definite**: All eigenvalues positive (local minimum in optimization)
- **Negative definite**: All eigenvalues negative (local maximum in optimization)
- **Indefinite**: Mixed eigenvalues (saddle point in optimization)

## Usage Examples

```python
# Basic matrix operations
from determinant import determinant
from minor import minor
from cofactor import cofactor
from adjugate import adjugate
from inverse import inverse

# Define a matrix
matrix = [[2, 1], [1, 2]]

# Calculate various properties
det = determinant(matrix)           # 3
min_mat = minor(matrix)            # [[2, 1], [1, 2]]
cof_mat = cofactor(matrix)         # [[2, -1], [-1, 2]]
adj_mat = adjugate(matrix)         # [[2, -1], [-1, 2]]
inv_mat = inverse(matrix)          # [[0.667, -0.333], [-0.333, 0.667]]

# Check definiteness
import numpy as np
from definiteness import definiteness
np_matrix = np.array(matrix)
def_type = definiteness(np_matrix)  # "Positive definite"
```

## Error Handling

All functions include comprehensive error handling:

- **TypeError**: For incorrect input types
- **ValueError**: For invalid matrix dimensions or empty matrices
- **None returns**: For mathematically invalid operations

## Dependencies

- **Files 0-4**: Pure Python implementation (no external dependencies)
- **File 5**: Requires NumPy for eigenvalue computation

## Testing

Each function includes extensive test cases covering:

- Edge cases (1×1 matrices, singular matrices)
- Error conditions (non-square matrices, invalid inputs)
- Mathematical correctness verification
- Numerical precision handling

## Applications

These implementations are foundational for:

- Computer graphics transformations
- Machine learning algorithms
- Numerical optimization
- Systems of linear equations
- Signal processing
- Physics simulations

## Author

Implementation completed as part of ALU Machine Learning curriculum, focusing on understanding the mathematical foundations of linear algebra operations.
