import sys
sys.path.append('../utils')
from utils import *
import numpy as np

def chardir(i, j, dire, mapp):
    if i + dire[0] < 0 or j + dire[1] < 0:
        return None
    try:
        return mapp[i+dire[0], j+dire[1]]
    except:
        return None

def rotatedir(dire):
    return (dire[1], -dire[0])

def traverse(pos, dire, mapp):
    yield pos, dire
    while True:
        char = chardir(*pos, dire, mapp)
        if char == '.':
            pos = (pos[0]+dire[0], pos[1]+dire[1])
            yield pos, dire
        elif char == '#':
            dire = rotatedir(dire)
            yield pos, dire
        else:
            break

lines = read_data()
mapp = np.array([list(line) for line in lines])
i, j = np.where(mapp == '^')
start = (int(i[0]), int(j[0]))
mapp[*start] = '.'
res = 0
for a in range(mapp.shape[0]):
    for b in range(mapp.shape[1]):
        if (a, b) == start or mapp[a, b] == '#':
            continue
        new_mapp = np.copy(mapp)
        new_mapp[a, b] = '#'
        path = set()
        for x in traverse(start, (-1, 0), new_mapp):
            if x in path:
                res += 1
                break
            path.add(x)
print(res)
copy_result(res)
