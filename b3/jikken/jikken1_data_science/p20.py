import numpy as np
import matplotlib.pyplot as plt

from p18 import separate_data
from p19 import cross_validation

def plot_mean_test_erms():
    x=[x for x in range(1,10)]
    mean_test_err=[]
    for m in range(1,10): 
        mean_test_err.append(cross_validation(m))
        print(".")
    plt.plot(x,mean_test_err)
    plt.show()

plot_mean_test_erms()
