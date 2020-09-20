#code
def SelectionSort(arr,n):
    for i in range(0,n):
        minpos = i
        for j in range(i,n):
            if(arr[j]<arr[minpos]):
                minpos = j
        arr[i],arr[minpos] = arr[minpos],arr[i]
        #or
        #temp = arr[minpos]
        #arr[minpos] = arr[i]
        #arr[i] = temp

#driver
arr = [5,2,8,6,9,1,4]
n = len(arr)
SelectionSort(arr,n)
print("Sorted array is :")
for i in range(n):
    print(arr[i],end=" ")