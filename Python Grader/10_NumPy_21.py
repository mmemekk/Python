import numpy as np

def sum_2_rows(M):
    evenrow=M[::2,:]
    oddrow=M[1::2,:]
    result=evenrow+oddrow

    return result

def sum_left_right(M):
    half=int((M.shape[1])/2)
    left=M[:,:half]
    right=M[:,half:]
    result=left+right

    return result

def sum_upper_lower(M):
    half=int(M.shape[0]/2)
    upper=M[:half,:]
    lower=M[half:,:]    
    result=upper+lower

    return result

def sum_4_quadrants(M):
    halfrow=int(M.shape[0]/2)
    halfcolumn=int(M.shape[1]/2)
    q1=M[:halfrow,:halfcolumn]
    q2=M[:halfrow,halfcolumn:]
    q3=M[halfrow:,:halfcolumn]
    q4=M[halfrow:,halfcolumn:]
    
    return q1+q2+q3+q4

def sum_4_cells(M):
   return M[::2,::2]+M[1::2,::2]+M[::2,1::2]+M[1::2,1::2]

def count_leap_years(y):
    years=y-543
    x=years[(np.mod(years,400)==0) | ((np.mod(years,4)==0) & (np.mod(years,100)!=0))]
    return x.shape[0]


exec(input().strip())