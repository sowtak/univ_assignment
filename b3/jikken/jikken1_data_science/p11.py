import numpy as np

from p7 import generate_matrix, generate_vector
from p8 import calc_coeff
from p9 import calc_polynomial


# Calculate E_rms
def calc_erms(N,M):
    data=np.loadtxt('N-%d.txt' % N, delimiter=' ')
    t=data[:,1]
    w=calc_coeff(M,N)
    y=calc_polynomial(M,N,w)
    
    sum=0
    for n in range(N):
        sum+=np.power(y[n]-t[n], 2)
    
    return np.sqrt(sum/N)
