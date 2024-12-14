import sys
sys.path.append('../utils')
from utils import *
import numpy as np
import itertools

def isValid(loc, mapp):
    if loc[0] in range(mapp.shape[0]) and loc[1] in range(mapp.shape[1]):
        return True
    return False

def mask(i, j, center, direction):
    columns = np.vstack([np.arange(i) for _ in range(j)])
    rows = np.transpose(np.vstack([np.arange(j) for _ in range(i)]))
    a = (rows - center[0]) / direction[0]
    b = (columns - center[1]) / direction[1]
    return (a == b).astype(int)

lines = read_data()
mapp = np.array([list(line) for line in lines])
vals = np.unique(mapp)
locs = np.zeros(mapp.shape)
for val in vals:
    if val == '.':
        continue
    indices = zip(*np.where(mapp == val))
    for x, y in itertools.combinations(indices, 2):
        locs += mask(*mapp.shape, x, (y[0] - x[0], y[1] - x[1]))
res = np.sum((locs > 0).astype(int))
print(res)
copy_result(res)
