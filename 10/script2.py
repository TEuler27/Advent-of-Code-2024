import sys
sys.path.append('../utils')
from utils import *
import numpy as np
from scipy.signal import convolve2d

def countTrails(i, j, mapp, k=0):
    if k == 9:
        return 1
    kernel = [[0,1,0],  
              [1,0,1],
              [0,1,0]]
    mask = np.zeros_like(mapp, dtype=bool) 
    mask[i,j] = True                    
    tot = 0
    indices = np.where(np.logical_and(convolve2d(mask, kernel, mode='same'), mapp == k + 1))
    for i in range(indices[0].shape[0]):
        coord = (indices[0][i], indices[1][i])
        tot += countTrails(*coord, mapp, k+1)
    return tot

lines = read_data()
mapp = np.array([list(map(int, list(line))) for line in lines])
res = 0
starts = np.where(mapp == 0)
for i in range(starts[0].shape[0]):
    res += countTrails(starts[0][i], starts[1][i], mapp)
print(res)
copy_result(res)
