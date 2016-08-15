import numpy as np
import matplotlib.pyplot as plt

data = np.array([[1, 1, 1],
                 [1, 1, 0],
                 [1, 0, 1],
                 [1, 0, 0]])

w1 = np.array([[ 1.5,  0.5],
               [-1.0, -1.0],
               [-1.0, -1.0]])

w2 = np.array([[-0.5],
               [ 1.0],
               [-1.0]])


for var in data:
    #hidden layer
    hidden_units = [1]
    for n in range(0, len(w1[0])):
        hidden_activation = np.sum(var * w1[:,n])
        if hidden_activation >= 0: hidden_units.append(1)
        else: hidden_units.append(0) 
    #out layer
    output = 1
    out_activation = np.sum(hidden_units * w2[:,0])
    if out_activation < 0: output = 0
    print('INPUT: ', var, 'HIDDEN: ', hidden_units, '| OUT: ', output)

