import numpy as np

def regulalization_polynomial_regression(A,lam,T):
    N=len(T)
    y=np.empty((N,1))
    I=np.eye(N)
    w=np.linalg.solve(A+lam*I, T)
    
def calc_erms_reg(M,x,t,w):

    N=len(t)
    y=calc_polynomial(M,x,w)
    
    sum=0
    for n in range(N):
        sum+=np.power(y[n]-t[n], 2)
    
    return np.sqrt(sum/N)
