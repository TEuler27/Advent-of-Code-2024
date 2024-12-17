import sys
sys.path.append('../utils')
from utils import *
from functools import cache

@cache
def rocks_production(time, num):
    if time == 0:
        return 1
    tot = 0 
    if num == 0:
        tot += rocks_production(time - 1, 1)
    elif len(str(num)) % 2 == 0:
        digits = len(str(num))
        tot += rocks_production(time - 1, int(str(num)[digits // 2:]))
        tot += rocks_production(time - 1, int(str(num)[:digits // 2]))
    else:
        tot += rocks_production(time - 1, num * 2024)
    return tot

line = read_data()[0]
rocks = line.split(' ')
rocks = list(map(int, rocks))
res = 0
for rock in rocks:
    res += rocks_production(75, rock)
print(res)
copy_result(res)
