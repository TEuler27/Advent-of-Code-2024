import sys
sys.path.append('../utils')
from utils import *
from collections import Counter
import re

lines = read_data()
a = []
b = []
i = 0
for line in lines:
    line = re.sub(' +', ' ', line)
    nums = *map(int, line.split(' ')),
    a.append(nums[0])
    b.append(nums[1])
ac = Counter(a)
bc = Counter(b)
res = 0
for num in ac.keys():
    if num not in bc.keys():
        continue
    else:
        res += num*ac[num]*bc[num]
print(res)
copy_result(res)
