import numpy as np
import sys
sys.path.append('../utils')
from utils import *

lines = read_data()
res = 0
for line in lines:
    line = *map(int, line.split(' ')),
    line = np.array(line)
    for i in range(len(line)):
        nline = np.delete(line, i)
        dif = np.diff(nline)
        if (dif > 0).all() or (dif < 0).all():
            if (abs(dif) <= 3).all():
                res += 1
                break
print(res)
copy_result(res)
