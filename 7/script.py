import sys
sys.path.append('../utils')
from utils import *

def counter(nums, goal, c = 0):
    if c == goal:
        return True 
    elif len(nums) == 0 or c> goal:
        return False
    else:
        return counter(nums[1:], goal, c+nums[0]) or counter(nums[1:], goal, c*nums[0])
    
lines = read_data()
res = 0
for line in lines:
    goal, nums = line.split(':')
    goal = int(goal)
    nums = *map(int,  nums[1:].split(' ')),
    if counter(nums[1:], goal, nums[0]):
        res += goal
print(res)
copy_result(res)
