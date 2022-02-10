"""
Write a program to count inversions in an array
Input: arr[] = {8, 4, 2, 1}
Output: 6
Explanation: Given array has six inversions:
(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).
"""

class Inversion:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    def count_inversion(self):
        """
        [A naive approach to count inversions in given array]
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        Returns:
            [int]: [Inversions count]
        """
        count = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.arr[i] > self.arr[j]:
                    count += 1

        return count


# Driver
arr = [8, 4, 2, 1] 
result = Inversion(arr, len(arr))

print(f"Number of inversions in arr {arr} is {result.count_inversion()}")
