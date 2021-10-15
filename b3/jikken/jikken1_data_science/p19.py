import numpy as np

from p12 import calc_coeff, generate_matrix,generate_vector,calc_erms
from p18 import separate_data

def calc_min_coeff(M,train, test, iteration=1000):
    
    min_erms=100000000
    for _ in range(iteration):
        x=train[:,0]
        t=test[:,1]
        w=calc_coeff(generate_matrix(M,x),generate_vector(M, train))
        E=calc_erms(M,x,t,w)
        
        if E<min_erms:
            min_erms=E

    #return min_coeff
    return min_erms

def cross_validation(M):
    mean_erms=[]
    for _ in range(5):
        train,test=separate_data()
        err=calc_min_coeff(M, train, test)
        mean_erms.append(err)

    return (np.sum(mean_erms)/5)

#print(cross_validation(3))
