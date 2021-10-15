import numpy as np

from p17 import generate_rand_int



def separate_data():
    a=generate_rand_int()
    data=np.loadtxt('N-20.txt')

    data_train=data[a!=5]
    data_test=data[a==5]
    return [data_train,data_test]

