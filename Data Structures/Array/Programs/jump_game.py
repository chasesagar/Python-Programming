"""
Given an array of integers where each element represents the max number of steps that can be made 
forward from that element. Write a function to return the minimum number of jumps to reach the 
end of the array (starting from the first element). If an element is 0, they cannot move through 
that element. If the end isn’t reachable, return -1.

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 9 -> 9)

"""
class ArrayGame:
    def __init__(self, arr: list = None, n: int = None):
        self.arr = arr
        self.n = n

    def minimum_jumps_to_reach_array_end_element(self):
        """
        [A program to to find minimum jumps to reach array end using recursion]
        Time complexity = O(n*n)
        Auxillary Space = O(1)
        Returns:
            [int]: [Minimum jumps to reach self.arr[n] from self.arr[o]]
        """
        return self.minimum_jumps(self.arr, 0, self.n-1)
    
    @staticmethod
    def minimum_jumps(arr, low, high):
        # base condition
        if high == 1: return 0
        if arr[low] == 0: return float('inf')

        min = float('inf')
        for i in range(low+1, high+1):
            if i <= (low + arr[low] + 1):
                jumps = ArrayGame.minimum_jumps(arr, i, high)
                if jumps != float('inf') and jumps + 1 < min:
                    min = jumps + 1

        return min

# Driver program to test above function
arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
res= ArrayGame(arr, len(arr))
print('Minimum number of jumps to reach, end is', res.minimum_jumps_to_reach_array_end_element())