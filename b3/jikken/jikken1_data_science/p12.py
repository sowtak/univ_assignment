import numpy as np


def generate_matrix(M, x):
    N=len(x)
    A=np.empty((M+1, M+1))
    for i in range(M+1):
        for j in range(M+1):
            sum=0
            for n in range(N):
                sum+=x[n]**(i+j)
            A[i][j]=sum
    return A


def generate_vector(M, data):
    N=len(data[:, 0])
    T=np.empty((M+1))
    for i in range(M+1):
        sum=0
        for n in range(N):
            sum+=(data[n][0]**i)*data[n][1]
        T[i]=sum
    return T


def calc_coeff(A,T):
    return np.linalg.solve(A,T)


def calc_polynomial(M,x,w):
    N=len(x)
    y=np.empty((N,1))
    for n in range(N):
        sum=0
        for j in range(M+1):
            sum+=w[j]*(x[n]**j)
        y[n]=sum
    
    return y


# Calculate E_rms
def calc_erms(M,x,t,w):
    N=len(t)
    y=calc_polynomial(M,x,w)
    
    sum=0
    for n in range(N):
        sum+=np.power(y[n]-t[n], 2)
    
    return np.sqrt(sum/N)


def minimize_erms(M, N, mode='train', iteration=1000):
    min_erms=100000000
    min_coeff=np.full((M+1,1), 100000000)
    data=np.loadtxt(f'N-%s.txt' % str(N), delimiter=' ')
    
    for _ in range(iteration):
        np.random.shuffle(data)

        if mode=='train':
            x=data[:N//2,0]
            t=data[:N//2,1]
            w=calc_coeff(generate_matrix(M,x),generate_vector(M,data[:N//2,]))
        else:
            x=data[N//2:,0]
            t=data[N//2:,1]
            w=calc_coeff(generate_matrix(M,x),generate_vector(M,data[N//2:,]))
        
        E=calc_erms(M,x,t,w)
        
        if E<min_erms:
            min_erms=E
            min_coeff=w

    #return min_coeff
    return min_erms
        

#print(minimize_erms(3,20,'train',10000))
