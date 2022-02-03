"""
A array of n elements which is first increasing and then may be decreasing, 
find the maximum element in the array.
Input: n = 9 arr[] = {1,15,25,45,42,21,17,12,11}
Output: 45
Explanation: Maximum element is 45.

"""


class Search:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    def biotonic_point(self):
        """
        [A program to find biotonic point using binary search]
        Time Complexity: O(Log(N))
        Auxiliary Space: O(1)
        Returns:
            [int]: [biotonic point]
        """
        low = 0
        high = self.n - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            if self.arr[mid] > self.arr[mid - 1] and self.arr[mid] > self.arr[mid + 1]:
                return self.arr[mid]
            elif self.arr[mid] < self.arr[mid - 1]:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def biotonic_search_recursion(self):
        """
        [A program to find biotonic point using binary search recursion]
        Time Complexity: O(Log(N))
        Auxiliary Space: O(1)
        Returns:
            [int]: [biotonic point]
        """
        arr = self.arr.copy()
        return self.binarySearch(arr, 0, self.n - 1)

    @classmethod
    def binarySearch(cls, arr, left, right):

        if left <= right:
            mid = (left + right) // 2

            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            if arr[mid] < arr[mid + 1]:
                return cls.binarySearch(arr, mid + 1, right)
            else:
                return cls.binarySearch(arr, left, mid - 1)

        return -1

    def biotonic_point_interation(self):
        """
        [A program to find biotonic point using binary search and interation]
        Time Complexity: O(N)
        Auxiliary Space: O(1)
        Returns:
            [int]: [biotonic point]
        """
        n = self.n - 1
        while n >= 0:
            if self.arr[n] >= self.arr[n - 1]:
                return self.arr[n]
            else:
                n -= 1

        return -1


# Driver
arr = [1, 15, 25, 45, 42, 21, 17, 12, 11]
print(f"Biotonic point is: {Search(arr, len(arr)).biotonic_point()}")
print(f"Biotonic point using recursion is: {Search(arr, len(arr)).biotonic_search_recursion()}")
print(f"Biotonic point using iteration is: {Search(arr, len(arr)).biotonic_point_interation()}")
