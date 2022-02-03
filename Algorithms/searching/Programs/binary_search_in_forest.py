"""
    Given an integer K and an array, height[] where height[i] denotes the height of the 
    ith tree in a forest. The task is to make a cut of height X from the ground such that 
    exactly K unit wood is collected. If it is not possible, then print -1 else print X.

    Input: height[] = {1, 2, 1, 2}, K = 2 
    Output: 1 
    Make a cut at height 1, the updated array will be {1, 1, 1, 1} and 
    the collected wood will be {0, 1, 0, 1} i.e. 0 + 1 + 0 + 1 = 2.

    Input: height = {1, 1, 2, 2}, K = 1 
    Output: -1  
"""


class Search:
    def __init__(self, height, n, k):
        self.height = height
        self.n = n
        self.k = k

    def binary_search_in_forest(self):
        height = self.height.copy()
        height.sort()

        low, high = 0, max(height)
        while low <= high:
            mid = low + ((high - low) // 2)
            collected = self.woodCollected(height, self.n, mid)

            if collected == self.k:
                return collected
            elif collected < self.k:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    @staticmethod
    def woodCollected(height, n, m):
        sum = 0
        for i in range(n - 1, -1, -1):
            if height[i] - m <= 0:
                break
            sum += height[i] - m

        return sum


# Driver code
height = [1, 2, 1, 2]
n = len(height)
k = 2

print(f"In order to collect {k} unit wood cut should be "
      f"make at {Search(height,n,k).binary_search_in_forest()}")
