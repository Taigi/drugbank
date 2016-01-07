from __future__ import  division
import numpy as np
from math import log



def shortest_path_measure(matrix):
    for x in np.nditer(matrix, op_flags=['readwrite']):
        x[...] = 10 - x
    return matrix


# Leakcock and Chodorow's Measure for converting shorthest path distance into the similarity

def leakcock_chodorow_measure(matrix):
    for x in np.nditer(matrix, op_flags=['readwrite']):
        if(x==0):
            x[...] = 1
        elif(x==-1):
            x[...] = 0
        else:
            val = -log(x/10)
            if np.isnan(val):
                print(x)
            x[...] = val
    return matrix

# matrix = numpy.load('dm_uw_classification.npy')
# from convertDistToSim import leakcock_chodorow_measure
# matrix = leakcock_chodorow_measure(matrix)
# print(matrix)
# numpy.save('sim_mat_uw_classification.npy',matrix)
#