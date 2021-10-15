import numpy as np

from p18 import separate_data

def linear_regression():
    train,test=separate_data()
    print(train,test)
    x=train[:,0]
    t=test[:,1]
    print(t)

linear_regression()
