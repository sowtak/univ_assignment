import numpy as np

from p7 import generate_matrix, generate_vector


def calc_coeff(M,N):
    A=generate_matrix(M,N)
    T=generate_vector(M,N)
    return np.linalg.solve(A,T)

print(calc_coeff(2,100))
