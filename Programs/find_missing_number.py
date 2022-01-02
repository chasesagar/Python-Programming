# A program to find missing number in python
import functools

class Solution:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    def calc_sum(self):
        return functools.reduce(lambda x, y: x+y, self.arr)

    def calc_sum_custom(self):
        count = 0
        for i in range(self.arr):
            count += i
        return count

    def missing_number(self):
        total = self.n * (self.n + 1) / 2
        return int(total - sum(self.arr))

#  Driver Code 

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    s = Solution(a,n)
    print(s.missing_number())
