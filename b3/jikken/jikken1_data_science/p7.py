import numpy as np


def generate_matrix(M, N=100):
    data=np.loadtxt('N-%d.txt' % N, delimiter=' ')
    A=np.empty((M+1, M+1))
    for i in range(M+1):
        for j in range(M+1):
            sum=0
            for n in range(N):
                sum+=data[n][0]**(i+j)
            A[i][j]=sum
    return A

def generate_vector(M, N=100):
    data=np.loadtxt('N-%d.txt' % N, delimiter=' ')
    T=np.empty((M+1))
    for i in range(M+1):
        sum=0
        for n in range(N):
            sum+=(data[n][0]**i)*data[n][1]
        T[i]=sum
    return T

#print(generate_matrix(2))
#print(generate_vector(2))
