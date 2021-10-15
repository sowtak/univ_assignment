import numpy as np
import matplotlib.pyplot as plt

x=np.random.rand(10,1)
y = np.sin(2 * np.pi * x) + np.random.normal(0, 0.1)
fig, ax = plt.subplots()
ax.set(xlabel='x', ylabel='y',
       title='')
ax.grid()
plt.plot(x,y,'o',c='black')
plt.show()
