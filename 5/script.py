import sys
sys.path.append('../utils')
from utils import *
import itertools

def less(a, b, ordering):
    if (a, b) in ordering:
        return True
    elif (b, a) in ordering:
        return False
    else:
        return True

lines = read_data()
ordering = set()
j = 0
for i, line in enumerate(lines):
    if line == '':
        j = i
        break
    else:
        ordering.add(tuple(line.split('|')))

res = 0
for line in lines[j+1:]:
    nums = line.split(',')
    if all(map(lambda x: less(x[0], x[1], ordering),itertools.combinations_with_replacement(nums, 2))): 
        res += int(nums[len(nums)//2])
print(res)
copy_result(res)
