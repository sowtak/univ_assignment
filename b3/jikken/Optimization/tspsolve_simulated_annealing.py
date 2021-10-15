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

def simulated_annealing():
    initial_ans=np.random()
    initial_temperature=
    num_initial_iteration=3000

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

def output_to_file(problem, method, neighbor, *coords):
    output_filename = cwd + "tentative_answer.txt"
    if not os.path.exists(cwd + output_filename):
        open(output_filename, 'w').close()
    with open(output_filename, 'a+') as f:
        f.write('#' + 'problem' + ' ' + ':' + problem + '\n')
        f.write('#' + 'method' + ' ' + ':' + method + '\n')
        f.write('#' + 'neighbor' + ' ' + ':' + neighbor + '\n')
        for i in range(len(coords)):
            f.write(str(coords[0]) + " " + str(coords[1]) + '\n')



    
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
