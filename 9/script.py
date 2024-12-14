import sys
sys.path.append('../utils')
from utils import *
import numpy as np

lines = read_data()
line = lines[0]
files = line[::2]
space = line[1::2]
files_infos = {i: int(char) for i, char in enumerate(list(files))}
files_id = sorted(files_infos.keys())
disk_size = np.sum(np.array(list(map(int,line))))
checksum = 0
moved = False
id_space = 0
for i in range(disk_size):
    if not moved:
        checksum += i*files_id[0]
        files_infos[files_id[0]] -= 1
        if files_infos[files_id[0]] <= 0:
            del files_id[0]
            if id_space < len(space):
                free_space = int(space[id_space])
                if free_space > 0:
                    moved = True
                id_space += 1
            if len(files_id) == 0:
                break
    else:
        checksum += i*files_id[-1]
        files_infos[files_id[-1]] -= 1
        if files_infos[files_id[-1]] <= 0:
            del files_id[-1]
            if len(files_id) == 0:
                break
        free_space -= 1
        if free_space == 0:
            moved = False
print(checksum)
copy_result(checksum)
