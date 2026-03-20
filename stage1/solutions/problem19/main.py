import sys
import json

def solve():
    nums = json.loads(sys.stdin.readline())
    
    squared_nums = [x * x for x in nums]
    squared_nums.sort()
    print(squared_nums)

if __name__ == "__main__":
    solve()
