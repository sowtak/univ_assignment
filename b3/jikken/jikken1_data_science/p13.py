import numpy as np
import matplotlib.pyplot as plt

from p12 import minimize_erms



### Problem 7.15 ###
### Sometimes fails. Please try again then.
def plot_train_losses():
    x=np.array([ x for x in range(1,10) ])
    y20,y50,y100=[],[],[]
    for m in range(1,10):
        err=minimize_erms(m,20,'train',100)
        y20.append(err)
    
    for m in range(1,10):
        err=minimize_erms(m,50,'train',100)
        y50.append(err)

    for m in range(1,10):
        err=minimize_erms(m,100,'train',100)
        y100.append(err)

    plt.plot(x,y20,c='r')
    plt.plot(x,y50,c='g')
    plt.plot(x,y100,c='b')
    plt.show()

plot_train_losses()

