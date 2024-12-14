import sys
sys.path.append('../utils')
from utils import *
import numpy as np
import itertools

def isValid(loc, mapp):
    if loc[0] in range(mapp.shape[0]) and loc[1] in range(mapp.shape[1]):
        return True
    return False

lines = read_data()
mapp = np.array([list(line) for line in lines])
vals = np.unique(mapp)
locs = set()
for val in vals:
    if val == '.':
        continue
    indices = zip(*np.where(mapp == val))
    for x, y in itertools.combinations(indices, 2):
        locs.add((2*x[0] - y[0], 2*x[1] - y[1]))
        locs.add((2*y[0] - x[0], 2*y[1] - x[1]))
locs = list(filter(lambda x: isValid(x, mapp), locs))
print(len(locs))
copy_result(len(locs))
