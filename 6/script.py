import sys
sys.path.append('../utils')
from utils import *
import numpy as np

def chardir(i, j, dire, mapp):
    try:
        return mapp[i+dire[0], j+dire[1]]
    except:
        return None

def rotatedir(dire):
    return (dire[1], -dire[0])

lines = read_data()
visited = set()
pos = None
dire = (-1, 0)
mapp = np.array([list(line) for line in lines])
for i in range(mapp.shape[0]):
    for j in range(mapp.shape[1]):
        if mapp[(i, j)] == '^':
            pos = (i, j)
            break
    if pos != None:
        break
visited.add(pos)
while True:
    char = chardir(*pos, dire, mapp)
    if char == '.' or char == '^':
        pos = (pos[0]+dire[0], pos[1]+dire[1])
        visited.add(pos)
    elif char == '#':
        dire = rotatedir(dire)
    else:
        break
print(len(visited))
copy_result(len(visited))
