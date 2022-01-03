# A program to rotate(ar[], d, n) that rotates arr[] of size n by d elements.

class ArrayRotation:
    def __init__(self, arr, d, n):
        self.arr = arr
        self.d = d
        self.n = n

    def array_rotation_using_temp_array(self):
        """
        [Method 1: Array rotation using temp array]
        Time complexity: O(n)
        Auxiliary Space : O(d)

        Returns:
            [list]: [A list of rotated array]
        """
        arr = self.arr.copy()
        temp_arr = arr[: self.d]
        for i in range(self.n - self.d):
            arr[i] = arr[self.d + i]

        return arr[: -self.d] + temp_arr

# Driver
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
s = ArrayRotation(arr, d, len(arr))
print(f"Clockwise array rotation by {d} elements is: {s.array_rotation_using_temp_array()} ")
