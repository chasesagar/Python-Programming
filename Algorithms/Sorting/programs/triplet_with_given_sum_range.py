"""
Write a program Count number of triplets in an array having sum in the range [a, b]
Input : arr[] = {8, 3, 5, 2} range = [7, 11]
Output : 1 There is only one triplet {2, 3, 5} having sum 10 in range [7, 11].
"""


class Count:
    def __init__(self, arr, n, limit):
        self.arr = arr
        self.n = n
        self.limit = limit

    def count_triplets(self):
        """
        [A naive approach to find all possible triplets in given range]
        Time complexity: O(n3)
        Auxiliary Space: O(1)
        Returns:
            [int]: [count of triplets found in given range]
        """
        count = 0
        for i in range(0, self.n):
            for j in range(i + 1, self.n):
                for k in range(j + 1, self.n):
                    if self.arr[i] + self.arr[j] + self.arr[k] in range(
                        self.limit[0], self.limit[1] + 1
                    ):
                        # print(f"Triplet is: {self.arr[i]}, {self.arr[j]}, {self.arr[k]}")
                        count += 1

        return count

    def count_triplets_efficient(self):
        """
        [An efficient approach to find all possible triplets in given range]
        Time complexity: O(n2)
        Auxiliary Space: O(1)
        Returns:
            [int]: [count of triplets found in given range]
        """
        arr = self.arr.copy()
        # Any O(NlogN) sorting algorithm
        arr.sort()

        return self.find_triplet_given_sum(
            arr, self.n, self.limit[1]
        ) - self.find_triplet_given_sum(arr, self.n, self.limit[0] - 1)

    @staticmethod
    def find_triplet_given_sum(arr, n, value):
        count = 0
        j = 0
        k = 0

        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j != k:
                temp_sum = arr[i] + arr[j] + arr[k]
                if temp_sum > value:
                    k -= 1
                else:
                    count += k - j
                    j += 1
        return count


# Driver
arr = [2, 7, 5, 3, 8, 4, 1, 9]
limit = [8, 16]

triplets = Count(arr, len(arr), limit)

print(f"Total possible triplets in given range {limit} is {triplets.count_triplets()}")
print(f"Total possible triplets in given range {limit} is {triplets.count_triplets_efficient()}")
