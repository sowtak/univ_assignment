import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# parse
cwd=os.getcwd()+ "\\"  # get current directory
print(cwd)
filename=sys.argv[1] # get input file name
iteration=int(sys.argv[2]) # get number of iteration
path=cwd+ filename 

num_cities = int(filename[3:-4]) # extract number from input file.

with open(path) as f:
    node=[list(map(int, line.rstrip().split())) for line in f.readlines()[6:-1] ]

# Calculate distance matrix
rows, cols = (num_cities,num_cities)
dist = np.array([[0]*cols] * rows)
for i in range(len(node)):
    for j in range(len(node)):
        if i != j:
            dist[i][j] = np.sqrt(pow(node[i][1] - node[j][1], 2) + pow(node[i][2] - node[j][2], 2))

# 7.2 iterate random search for specified number of times
def random_swap(iteration):
    interval=1000
    init_ans=np.random
    fn, fn2='', ''
    for i in range(iteration+1):
        if i%interval == 0:
            fn=f'random-%s.dat' % (str(i)) 
            fn2=f'transition_hill-%s.txt' % str(iteration)
            if not os.path.exists(cwd + fn):
                open(fn, 'w').close()
            if not os.path.exists( cwd + fn2):
                open(fn2, 'w').close()
        arr=np.random.permutation(num_cities) # uses mersenne twister algorithm internally.
        arr=[x-1 for x in arr]
        cost=0

        f= open(fn, 'w+')
        for j in range(len(arr)):
            if j != len(arr)-1:
                cost+=dist[arr[j]][arr[j+1]]
            else:
                cost+=dist[arr[-1]][arr[0]]
            f.write(str(node[arr[j]][1]) + " " + str(node[arr[j]][2])+ '\n')
        f.close()
        
        with open(fn, 'a+') as f:
            f.write(str(node[arr[0]][1]) + " " + str(node[arr[0]][2]) + '\n')
       
        min_cost=min(cost,min_cost)
        
        if i%interval == 0:
            with open(fn2, 'a+') as f:
                f.write(str(min_cost) + '\n')

def two_opt_neighbor(iteration):


# read cost data from text file and plot them.
def show_transition(num_iteration):
    f=open(f'transition_hill-%s.txt' % (str(num_iteration)), "r")
    lines=f.readlines()
    x = ([i+1 for i in range(len(lines))])
    y = np.array([e for e in lines])

    plt.title("Score transition")
    plt.xlabel("Number of iteration")
    plt.ylabel("Score")
 #   plt.yticks(ticks=y, rotation='vertical')
    plt.plot(x,y,'-o' )
    plt.show()
    
#node_plot=[[node[i][1], node[i][2]] for i in range(num_cities)]
#node_plot=np.array(node_plot)
#plt.style.use('ggplot')
#plt.figure(figsize=(4,4))
#plt.plot(node_plot[:, 0], node_plot[:, 1], 'o')
#plt.show()

if sys.argv[3][0] == 'r':
    random_swap(iteration)
    show_transition(iteration)
elif sys.argv[3][0] == 't':
    two_opt_neighbor(iteration)
    show_transition(iteration)
