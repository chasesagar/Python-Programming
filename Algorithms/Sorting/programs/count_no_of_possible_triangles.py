"""
Write a program to calculate no of possible triangles in given array
Input: arr= {4, 6, 3, 7}
3, 4, 6, 7
Output: 3
Explanation: There are three triangles possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}. 
"""

class Geometry:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    def possible_triangles_brute(self):
        """
        [brute force approach to find total number of triangles in the given array]
        Time Complexity: O(N^3)
        Space Complexity: O(1)
        Returns:
            [int]: [total number of available triangles in yhe given array]
        """
        arr = self.arr.copy()
        count = 0
 
        for i in range(self.n):
            for j in range(i + 1, self.n):
                for k in range(j + 1, self.n):
                    # Sum of two sides is greater than the third
                    if (arr[i] + arr[j] > arr[k] and
                        arr[i] + arr[k] > arr[j] and
                        arr[k] + arr[j] > arr[i]):
                        count += 1
        return count


# Driver
arr = [4, 6, 3, 7]
geometry  = Geometry(arr, len(arr))
print("Total possible triangles are {}".format(geometry.possible_triangles_brute()))