import numpy as np
import sys
sys.path.append('../utils')
from utils import *

lines = read_data()
res = 0
for line in lines:
    line = *map(int, line.split(' ')),
    line = np.array(line)
    dif = np.diff(line)
    if (dif > 0).all() or (dif < 0).all():
        if (abs(dif) <= 3).all():
            res += 1
print(res)
copy_result(res)
