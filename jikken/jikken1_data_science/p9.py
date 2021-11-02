import numpy as np
import matplotlib.pyplot as plt

from p7 import generate_matrix, generate_vector
from p8 import calc_coeff


def calc_polynomial(M,N, w):
    data=np.loadtxt('N-%d.txt' % N, delimiter=' ')
    x=data[:,0]
    y=np.empty((N,1))

    for n in range(N):
        sum=0
        for j in range(M):
            sum+=w[j]*(x[n]**j)
        y[n]=sum
    
    return y


data=np.loadtxt('N-%d.txt' % 100, delimiter=' ')
x,y=data[:, 0],data[:, 1]
fig, ax = plt.subplots()
ax.set(xlabel='x', ylabel='y',title='')
ax.grid()
plt.axis([0,1,-1, 1])

# polynomial
plt.plot(x,calc_polynomial(100,100,calc_coeff(100,100)),'o', color='red')
# actual data
plt.plot(x,y,'o', color='blue')

plt.show()
