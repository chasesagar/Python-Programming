"""
Write a program to find left most and right most index of the given element
    Input: N = 9
           V[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}
           X = 5
    Output: 2 5 and if not found -1 -1 
"""


class Search:
    def __init__(self, arr, n, x):
        self.arr = arr
        self.n = n
        self.x = x

    def find_left_and_rightmost_index(self):
        """
        [A program to find leftmost and rightmost index of given element]
        Time Complexity: O(Log(N))
        Auxiliary Space: O(1)
        Returns:
            [str]: [leftmost and rightmost index of k]
        """
        low = 0
        high = self.n - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if (self.arr[mid] == self.x) and (self.arr[mid-1] < self.x or mid-1 == -1 ):
                left_most = mid
                right_most = mid
                for i in range(mid + 1, self.n):
                    if self.arr[i] == self.x:
                        right_most += 1
                return f"{left_most}, {right_most}"

            elif self.arr[mid] < self.x:
                low = mid + 1
            else:
                high = mid - 1

        return f"-1, -1"


# Driver
arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
x = 5

print(
    f"Leftmost and rightmost index of element {x} in given array "
    f"is {Search(arr, len(arr), x).find_left_and_rightmost_index()}"
)
