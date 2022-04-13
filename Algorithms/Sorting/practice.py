def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

def recursive_bubble_sort(arr):
    if len(arr) == 1:
        return arr
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    return recursive_bubble_sort(arr[:-1]) + [arr[-1]]

print(selection_sort([5,2,4,6,1,3]))
print(recursive_bubble_sort([5,2,4,6,1,3]))