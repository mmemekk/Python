import numpy as np

def mult_table(nrows,ncols):
    A=np.arange(1,ncols+1)
    B=np.arange(1,nrows+1).reshape(nrows,1)
    
    return A*B


exec(input().strip())
