# A program to find frequency of each element in a limited range array in less than O(n) time

class ArrayBasic:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    def count_frequency_sorted(self):
        """
        [A program to calculate frequency of elements in a sorted array]
        Time complexity: O(n)
        Auxiliary space: O(1)
        """
        index = 1
        frequency = 1
        while index < self.n:
            if self.arr[index-1] == self.arr[index]:
                index += 1
                frequency += 1
            else:
                print(f"Element {self.arr[index-1]} occur {frequency} times")
                index += 1
                frequency = 1

        print(f"Element {self.arr[index-1]} occur {frequency} times")

# Driver
arr = [10, 20, 30, 30, 30, 40, 50, 50, 50, 50, 70 ]
result = ArrayBasic(arr, len(arr))
result.count_frequency_sorted()