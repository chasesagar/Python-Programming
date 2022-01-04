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
        if self.d <= 0:
            return self.arr

        arr = self.arr.copy()
        temp_arr = arr[: self.d]
        for i in range(self.n - self.d):
            arr[i] = arr[self.d + i]

        return arr[: -self.d] + temp_arr

    def array_rotation_one_by_one(self):
        """
        [Method 2: Array rotation one by one using loop]
        Time complexity : O(n * d)
        Auxiliary Space : O(1)
        Returns:
            [list]: [A list of rotated array]
        """
        arr = self.arr.copy()
        for i in range(self.d):
            self._left_rotate_by_one(arr, self.n)

        return arr

    def array_rotation_using_reversal_algorithm(self):
        arr = self.arr.copy()

        # In case d is zero condition handler
        if self.d == 0:
            return -1
        # In case rotating factor is greater than length of array
        d = self.d % self.n

        self._reverse_array(arr, 0, d - 1)
        self._reverse_array(arr, d, self.n - 1)
        self._reverse_array(arr, 0, self.n - 1)

        return arr

    @staticmethod
    def _left_rotate_by_one(arr, n):
        temp = arr[0]
        for i in range(n - 1):
            arr[i] = arr[i + 1]
        arr[-1] = temp

    @staticmethod
    def _reverse_array(arr, start, end):
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp

            start += 1
            end -= 1


# Driver
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
s = ArrayRotation(arr, d, len(arr))
print(
    f"Clockwise array rotation by {d} elements using temp array approach is: {s.array_rotation_using_temp_array()} "
)
print(
    f"Clockwise array rotation by {d} elements using one by one method is: {s.array_rotation_one_by_one()} "
)
print(
    f"Clockwise array rotation by {d} elements using reversal algorithm is: "
    f"{s.array_rotation_using_reversal_algorithm()}"
)
