import sys
sys.path.append('../utils')
from utils import *
import numpy as np
import regex as re

lines = read_data()
dataset = list(map(lambda x: list(x),lines))
mat = np.array(dataset)
res = 0
for i in range(mat.shape[0]):
    res += len(re.findall(r'XMAS|SAMX', ''.join(mat[i, :]),overlapped=True))
    res += len(re.findall(r'XMAS|SAMX', ''.join(np.diagonal(mat, -i)),overlapped=True))
    res += len(re.findall(r'XMAS|SAMX', ''.join(np.diagonal(np.rot90(mat), i)),overlapped=True))
for j in range(mat.shape[1]):
    res += len(re.findall(r'XMAS|SAMX', ''.join(mat[:, j]),overlapped=True))
    res += len(re.findall(r'XMAS|SAMX', ''.join(np.diagonal(mat, j)),overlapped=True))
    res += len(re.findall(r'XMAS|SAMX', ''.join(np.diagonal(np.rot90(mat), -j)),overlapped=True))
res -= len(re.findall(r'XMAS|SAMX', ''.join(np.diagonal(mat, 0)),overlapped=True))
res -= len(re.findall(r'XMAS|SAMX', ''.join(np.diagonal(np.rot90(mat), 0)),overlapped=True))
print(res)
copy_result(res)
