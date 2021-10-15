import matplotlib.pyplot as plt
import numpy as np


# Data for plotting
x = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * x)

fig, ax = plt.subplots()
ax.plot(x, s)

ax.set(xlabel='x', ylabel='y',
       title='')
ax.grid()

#fig.savefig("test.png")
plt.show()
