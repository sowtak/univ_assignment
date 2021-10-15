import numpy as np


def generate_data_data(A=[10,20,50,100]):
    for i in A:
        x=np.random.rand(i,1)
        y = np.sin(2 * np.pi * x) + np.random.normal(0, 0.1)
        mat=np.column_stack((x, y))   
        print(mat)
        print()
        np.savetxt(f'N-%s.txt' % (str(i)), mat)

generate_data_data()



