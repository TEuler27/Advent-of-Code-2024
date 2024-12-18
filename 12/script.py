import sys
sys.path.append('../utils')
from utils import *
import numpy as np
from scipy.signal import convolve2d

def flood(i, j, mapp, visited):
    start = (i, j)
    def subflood(i, j, mapp, prec=None):
        if prec == None:
            visited[(i, j)] = set()
        else:
            visited[(i, j)] = set([prec])
        char = mapp[i, j]
        kernel = [[0,1,0],  
              [1,0,1],
              [0,1,0]]
        mask = np.zeros_like(mapp, dtype=bool) 
        mask[i,j] = True                    
        tot = 0
        indices = np.where(convolve2d(mask, kernel, mode='same'))
        for k in range(len(indices[0])):
            index = int(indices[0][k]), int(indices[1][k])
            if mapp[*index] == char:
                visited[(i, j)].add(index)
                if index not in visited.keys():
                    subflood(*index, mapp)
        return 
    subflood(i, j, mapp)
    return visited

def perimeter(points):
    per = 0
    for x in points:
        per += 4 - len(points[x])
    return per

lines = read_data()
mapp = np.array([list(line) for line in lines])
areasTypes = np.unique(mapp)
res = 0
for char in areasTypes:
    wh = np.where(mapp == char)
    locs = set([(int(wh[0][i]), int(wh[1][i])) for i in range(len(wh[0]))])
    while True:
        try:
            index = locs.pop()
        except:
            break
        region = flood(*index, mapp, {})
        print(char, len(region), perimeter(region))
        res += perimeter(region) * len(region)
        locs.difference_update(set(region.keys()))
print(res)
copy_result(res)
