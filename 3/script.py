import sys
sys.path.append('../utils')
import re
from utils import *

lines = read_data()
res = 0
for line in lines:
    muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
    for mul in muls:
        nums = re.findall(r'\d{1,3}', mul)
        nums = *map(int, nums),
        res += nums[0] * nums[1]
print(res)
copy_result(res)
