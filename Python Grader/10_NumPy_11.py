import numpy as np

def get_column_from_bottom_to_top( A, c ):
    return A[:,c][::-1]

def get_odd_rows( A ):
    return A[1::2]

def get_even_column_last_row( A ):
    return A[A.shape[0]-1,::2]

def get_diagonal1( A ):
    return A.diagonal()

def get_diagonal2( A ):
    return np.array([A[i,-i-1] for i in range(len(A))])

exec(input().strip())



