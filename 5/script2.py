import sys
sys.path.append('../utils')
from utils import *
import functools
import graphlib

lines = read_data()
ordering = set()
j = 0
graph = {}
for i, line in enumerate(lines):
    if line == '':
        j = i
        break
    else:
        a, b = *map(int, line.split('|')),
        try:
            graph[a].add(b)
        except:
            graph[a] = set([b])
res = 0
for line in lines[j+1:]:
    nums = list(map(int, line.split(',')))
    ts = graphlib.TopologicalSorter({k : graph[k] for k in graph.keys() if k in nums})
    ordered = list(ts.static_order())
    sorted_nums = sorted(nums, key = lambda x: ordered.index(x), reverse=True)
    if nums != sorted_nums:
        nums.sort(key = lambda x: ordered.index(x), reverse = True) 
        res += nums[len(nums) // 2]
print(res)
copy_result(res)
