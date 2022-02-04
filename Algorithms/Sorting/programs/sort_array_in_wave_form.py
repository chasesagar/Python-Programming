""" 
Write a program to sort an array in wave form.
    Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
    Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
                    {20, 5, 10, 2, 80, 6, 100, 3} OR
                    any other array that is in wave form

"""


class Sort:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    def sort_in_wave(self):
        """
        [A program to sort array in wave form using sort inbuilt method]
        Time Complexity: O(nLogn)
        Auxiliary Space: O(1)
        Returns:
            [list]: [wave form array list]
        """
        arr = self.arr.copy()
        arr.sort()

        for i in range(0, self.n, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

        return arr


# Driver
arr = [10, 5, 6, 3, 2, 20, 100, 80]
sort = Sort(arr, len(arr))
print(f"In wave form array: {sort.sort_in_wave()}")
