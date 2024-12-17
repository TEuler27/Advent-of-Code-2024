import sys
sys.path.append('../utils')
from utils import *

def blink(rocks):
    added = 0
    copy_rocks = rocks[:]
    for i, rock in enumerate(copy_rocks):
        if rock == 0:
            rocks[i + added] = 1
        elif len(str(rock)) % 2 == 0:
            digits = len(str(rock))
            rocks[i + added] = int(str(rock)[:digits // 2])
            rocks.insert(i + added + 1, int(str(rock)[digits // 2:]))
            added += 1
        else:
            rocks[i + added] = rock * 2024
    return rocks

line = read_data()[0]
rocks = line.split(' ')
rocks = list(map(int, rocks))
for i in range(25):
    rocks = blink(rocks)
print(len(rocks))
copy_result(len(rocks))
