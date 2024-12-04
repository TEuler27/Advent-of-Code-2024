import sys
sys.path.append('../utils')
from utils import *
import regex as re

lines = read_data()
ncols = len(lines[0])
nrows = len(lines)
regcases = [f'S.S.{{{ncols-3}}}.A..{{{ncols-3}}}M.M',
            f'M.M.{{{ncols-3}}}.A..{{{ncols-3}}}S.S',
            f'M.S.{{{ncols-3}}}.A..{{{ncols-3}}}M.S',
            f'S.M.{{{ncols-3}}}.A..{{{ncols-3}}}S.M']
collapsed = ''.join(lines)
res = 0
for regcase in regcases:
    matches = re.finditer(regcase, collapsed, overlapped=True)
    for match in matches:
        if match.start() % ncols <= ncols - 3 and match.start() % nrows <= nrows -3:
            res += 1
print(res)
copy_result(res)
