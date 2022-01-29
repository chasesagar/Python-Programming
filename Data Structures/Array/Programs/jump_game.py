"""
Given an array of integers where each element represents the max number of steps that can be made 
forward from that element. Write a function to return the minimum number of jumps to reach the 
end of the array (starting from the first element). If an element is 0, they cannot move through 
that element. If the end isn’t reachable, return -1.

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 9 -> 9)

"""

from cmath import inf


class ArrayGame:
    def __init__(self, arr: list = None, n: int = None):
        self.arr = arr
        self.n = n

    def minimum_jumps_to_reach_array_end_element(self):
        self.minimum_jumps(self.arr, 0, self.n)
    
    @staticmethod
    def minimum_jumps(arr, low, high):
        # base condition
        if high == 1: return 0
        if arr[low] == 0: return float('inf')

        min = float('inf')
        for i in range(low, high):
            if i <= arr[low]:
                jumps = ArrayGame.minimum_jumps(arr, arr[])

        