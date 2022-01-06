# A program to rearrange array in alternating positive & negative items with O(1) extra space


class ArrayRearrange:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    def rearrange_array(self):
        arr = self.arr.copy()
        out_of_place = -1
        for i in range(self.n):

            if out_of_place == -1:
                # conditions for A[i] to
                # be in out of place
                if (arr[i] >= 0 and i % 2 == 0) or (arr[i] < 0 and i % 2 == 1):
                    out_of_place = i

            if out_of_place >= 0:
                if (arr[i] >= 0 and arr[out_of_place] < 0) or (arr[i] < 0 and arr[out_of_place] >= 0):
                    arr = self.right_rotate(arr, out_of_place, i)
                    if i - out_of_place > 2:
                        out_of_place += 2
                    else:
                        out_of_place = -1
        
        return arr

    @staticmethod
    def right_rotate(arr, out_of_place, cur):
        temp = arr[cur]
        for i in range(cur, out_of_place, -1):
            arr[i] = arr[i - 1]
        arr[out_of_place] = temp
        return arr

# Driver Code
arr = [-5, -2, 5, 2, 4,7, 1, 8, 0, -8]

s= ArrayRearrange(arr, len(arr))
print(f"Rearranged array is: {s.rearrange_array()}")