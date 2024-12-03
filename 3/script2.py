import sys
sys.path.append('../utils')
import re
from utils import *
from pprint import pprint

def compute_muls(string):
    res = 0
    muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', string)
    for mul in muls:
        nums = re.findall(r'\d{1,3}', mul)
        nums = *map(int, nums),
        res += nums[0] * nums[1]
    return res

lines = read_data()
line = ''.join(lines)
res = 0
donts = line.split('don\'t()')
for i, dont in enumerate(donts):
    if i == 0:
        res += compute_muls(dont)
    else:
        dos = dont.split('do()')
        for j, do in enumerate(dos):
            if j == 0:
                continue
            else:
                res += compute_muls(do)
print(res)
copy_result(res)
