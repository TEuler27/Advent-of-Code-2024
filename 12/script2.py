import sys
sys.path.append('../utils')
from utils import *
import numpy as np
from scipy.signal import convolve2d
import pprint
import copy

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

def calcOutline(region):
    vectors = {}
    vertices = [(0,0),(0,1),(1,1),(1,0)]
    sides = [(0,1),(1,0),(0,-1),(-1,0)]
    for point in region:
        for v, s in zip(vertices, sides):
            start = (point[0]+v[0], point[1]+v[1])
            opposite_start = (start[0] + s[0], start[1] + s[1])
            opposite_dir = (-s[0], -s[1])
            if opposite_start in vectors.keys():
                if opposite_dir in vectors[opposite_start]:
                    vectors[opposite_start].remove(opposite_dir)
                else:
                    try:
                        vectors[start].add(s)
                    except:
                        vectors[start] = set([s])
            else:
                try:
                    vectors[start].add(s)
                except:
                    vectors[start] = set([s])
    vectors = {key: list(vectors[key]) for key in vectors.keys() if len(vectors[key]) > 0}
    return vectors

def sides(outline, start = None):
    corners = 0
    if start == None:
        c = list(outline.keys())[0]
        if len(outline[c]) > 1:
            for i, d in enumerate(outline[c]):
                co = copy.deepcopy(outline)
                del co[c][i]
                new_corners = sides(co, start = ((c[0], c[1]), d))
                if new_corners > corners:
                    corners = new_corners
            return new_corners
        else:
            d = outline[c][0]
    else:
        c, d = start
    isFirst = True
    while True:
        next_c = (c[0] + d[0], c[1] + d[1])
        if next_c not in outline.keys():
            break
        if len(outline[next_c]) > 1:
            best_corners = corners
            for i, next_d in enumerate(outline[next_c]):
                co = copy.deepcopy(outline) 
                del co[next_c][i]
                t = sides(co, start = ((next_c[0], next_c[1]), next_d))
                if corners + t + 1 > best_corners:
                    best_corners = corners + t + 1
            return best_corners
        else:
            next_d = outline[next_c][0]
        if d[0] * next_d[0] + d[1] * next_d[1] == 0:
            corners += 1
        if not isFirst:
            del outline[c]
        else:
            isFirst = False
        c = next_c
        d = next_d
    del outline[c]
    if len(outline) == 0:
        return corners
    else:
        return corners + sides(outline)

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
        outline = calcOutline(region)
        res += sides(copy.deepcopy(outline)) * len(region)
        locs.difference_update(set(region.keys()))
print(res)
copy_result(res)
