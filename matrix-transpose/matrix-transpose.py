import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.asarray(A)
    A_t = np.zeros((A.shape[1], A.shape[0]))
     
    for row in range(A.shape[0]):
        for column in range(A.shape[1]):
            A_t[column][row] = A[row][column] 
    
    return A_t
