import numpy as np

def p(x):
    logit=-3.98+(0.1*x[:,0])+(0.5*x[:,1])
    value=1/(1+np.exp((-1)*logit))
    return value


exec(input().strip())