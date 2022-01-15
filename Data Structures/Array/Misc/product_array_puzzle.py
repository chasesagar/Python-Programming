# Product of array except itself
"""
    Given an array arr[] of n integers, construct a Product Array prod[] (of same size) such 
    that prod[i] is equal to the product of all the elements of arr[] except arr[i].
    Input: arr[]  = {10, 3, 5, 6, 2}
    Output: prod[]  = {180, 600, 360, 300, 900}
"""

from tkinter import N


class ArrayBasic:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    @staticmethod
    def reduce(function, iterable, initializer=None):
        """
        [A utility reduce function, similar to functools reduce method]
        Args:
            function ([with two arguments])
            iterable ([list,tuple, string])
            initializer ([any], optional): Defaults to None.

        Returns:
            [type]: [description]
        """
        it = iter(iterable)
        value = next(it) if initializer is None else initializer
        for element in it:
            value = function(value, element)
        return value

    def product_using_division(self):
        """
        [A program to solve product array puzzle using division approach]
        Time complexity: O(n)
        Auxillary space: O(1)
        Returns:
            [list]: [A list of product array puzzle result]
        """
        arr = self.arr.copy()
        total = self.reduce(lambda a,b: a*b, arr)

        for i in range(self.n):
            arr[i] = total // arr[i]

        return arr

    def product_array_without_division(self):
        """
        [A program to solve product array puzzle without division operator in O(n) time.]
        Time complexity: O(n)
        Auxillary space: O(n)
        Returns:
            [list]: [A list of product array puzzle result]
        """
        arr = self.arr.copy()

        # Base case
        if self.n == 0: return 

        # Allocate memory for temporary arrays
        left = [0]*self.n
        right = [0]*self.n

        # prodcut array
        prod = [0]*self.n

        left[0] = 1
        right[self.n-1] = 1

        # construct the left array
        for i in range(1, self.n):
            left[i] = arr[i-1] * left[i-1]

        for j in range(self.n-2, -1, -1):
            right[j] = arr[j+1] * right[j+1]

        for i in range(self.n):
            prod[i] = left[i] * right[i]

        return prod


    def product_array_without_division_and_less_space(self):
        """
        [A program to solve product array puzzle without division operator in O(n) time.]
        Time complexity: O(n)
        Auxillary space: O(n) Even though the extra arrays are removed, the space complexity remains O(n), 
                         as the product array is still needed.
        Returns:
            [list]: [A list of product array puzzle result]
        """
        arr = self.arr.copy()
        temp = 1
        prod = [1 for i in range(self.n)]

        for i in range(1,self.n):
            prod[i] = arr[i-1] * prod[i-1]

        for j in range(self.n-2, -1, -1):
            temp = temp * arr[j+1]
            prod[j] = temp * prod[j]
        
        return prod


# Driver
arr = [10, 3, 5, 6, 2]
res = ArrayBasic(arr, len(arr))
print(f"Prodduct array puzzle solution using division approach: {res.product_using_division()}")
print(f"Prodduct array puzzle solution using extra space approach: {res.product_array_without_division()}")
print("Prodduct array puzzle solution using less space" 
      f"approach: {res.product_array_without_division_and_less_space()}")