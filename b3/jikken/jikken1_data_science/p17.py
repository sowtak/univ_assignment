import numpy as np


def generate_rand_int():
    a=np.empty((1,20))
    while True:
        f=False
        a=np.random.randint(1,6,20)
        for i in range(1,6):
            if i not in a:
                f=True
                break
        if f: continue
        else: return a

#print(generate_rand_int())
