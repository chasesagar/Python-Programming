# code
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # double slash meany it give an integer value not float one.
        # creating sub lists
        lefthalf = arr[:mid]  # creates an array called lefthalf containing elements before mid
        righthalf = arr[
            mid:
        ]  # creates an array contains elements after mid in arr and store them in this array righthalf
        # recursion call
        MergeSort(lefthalf)
        MergeSort(righthalf)

        i = j = k = 0
        # comparing and sorting lefthalf and righthalf
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i + 1
            else:
                arr[k] = righthalf[j]
                j = j + 1
            k = k + 1
        # below while loops for the left element to fill it in his place.
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j + 1
            k = k + 1


# driver

arr = [5, 2, 7, 9, 4, 6, 2, 1, 0]
MergeSort(arr)
for i in range(0, len(arr)):
    print(arr[i], end=" ")
