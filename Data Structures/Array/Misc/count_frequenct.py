# A program to calculate frequency of array elements

class ArrayBasic:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    def calculate_frequency_hash_map(self):
        """
        [A program to calculate counting frequency of array elements]
        Time complexity: O(n)
        Auxiliary space: O(n)
        Returns:
            [dict]: [A dict with count]
        """
        hash_map = {}

        for i in self.arr:
            hash_map[i] = 1 if hash_map.get(i) == None else hash_map[i] + 1

        return hash_map

# Driver
arr = [10, 20, 20, 10, 10, 20, 5, 20]

result = ArrayBasic(arr, len(arr))
print(f"Frequency of array elements is: {result.calculate_frequency_hash_map()}")