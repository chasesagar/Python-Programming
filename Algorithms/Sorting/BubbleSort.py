#code
def BubbleSort(arr,n):
    for i in range(0,n):
        swapped = False
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if(swapped == False):
            break


#driver
arr = [5,2,7,9,4,6,2,1,0]
n = len(arr)
BubbleSort(arr,n)
for i in range(0,n):
    print(arr[i], end = " ")

#theory
"""
In place sorting algorithm
Stable Sort
Worst time Complexity O(n*n) when reverse sorted
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
"""