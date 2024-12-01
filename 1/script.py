import numpy as np
import re
import sys
sys.path.append('../utils')
from utils import *

lines = read_data()
a = []
b = []
for line in lines:
    line = re.sub(' +', ' ', line)
    nums = *map(int, line.split(' ')),
    a.append(nums[0])
    b.append(nums[1])
a =  np.array(sorted(a))
b = np.array(sorted(b))
res = np.sum(np.abs(a-b))
copy_result(res)
print(res)
