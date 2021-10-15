import os
import sys
import numpy as np
import matplotlib.pyplot as plt

cwd=os.getcwd() # get current directory
filename=sys.argv[1] # get input file name
method=sys.argv[2] # choose a method to use
path=cwd+ "\\" + filename # / in UNIX

num_cities = int(filename[3:-4]) # extract the number of cities from input file.

f=open(path)
node=[list(map(int, line.rstrip().split())) for line in f.readlines()[6:-1] ]
f.close()

# Calculate distance matrix
rows, cols = (num_cities,num_cities)
dist = np.array([[0]*cols] * rows)

for i in range(len(node)):
    for j in range(len(node)):
        if i != j:
            dist[i][j] = np.sqrt(pow(node[i][1] - node[j][1], 2) + pow(node[i][2] - node[j][2], 2))

# Functions

# Functions end

node_plot=[[node[i][1], node[i][2]] for i in range(num_cities)]
node_plot=np.array(node_plot)
plt.style.use('ggplot')
plt.figure(figsize=(4,4))
plt.plot(node_plot[:, 0], node_plot[:, 1], 'o')
plt.show()
