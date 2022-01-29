# A program to Search insert position of K in a sorted array

class Search:
    def __init__(self, arr, n, k):
        self.arr = arr
        self.n = n
        self.k = k

    def search_insert_pos_linear(self):
        """
        [Search insert postion of k in a sorted array using linear search approach]
        Time Complexity: O(N)
        Auxiliary Space: O(1)
        Returns:
            [int]: [insert position of k]
        """
        for i in range(self.n):
            if self.arr[i] == self.k:
                return i
            if self.arr[i] > self.k:
                return i
        return self.n

    def search_insert_pos_binary(self):
        """
        [Search insert postion of k in a sorted array using binary search approach]
        Time Complexity: O(logN)
        Auxiliary Space: O(1)
        Returns:
            [int]: [insert position of k]
        """
        low = 0
        high = self.n-1

        while low <= high:
            mid = (low + high) // 2

            if self.k == self.arr[mid]:
                return mid
            elif self.k < self.arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return high + 1

arr = [1,3,5,6]
k = 8
res = Search(arr, len(arr), k)
print(f"Insert position of k in sorted array is: {res.search_insert_pos_linear()}")
print(f"Insert position of k in sorted array is: {res.search_insert_pos_binary()}")