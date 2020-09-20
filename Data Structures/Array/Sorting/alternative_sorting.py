""" Alternative Sorting
    input = [7,1,2,3,4,5,6]
    output = [7,1,6,2,5,3,4]
"""
def AlternateSort(arr,n):
    QuickSort(arr,0,n-1)
    i = 0 
    j = n-1
    while(i<j):
        print(arr[j],end=" ")
        j -= 1
        print(arr[i],end=" ")
        i += 1
        #if total elements in array is odd print last middle element
    if (n%2 != 0):
        print(arr[i])

def QuickSort(arr,low,high):
    if(low<high):
        pi = partition(arr,low,high)

        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)

        return arr

        

def partition(arr,low,high):
    pivot = arr[high]
    pindex = low-1

    for i in range(low,high):
        if (arr[i]<pivot):
            pindex += 1
            arr[i],arr[pindex] = arr[pindex],arr[i]
        
    arr[pindex+1],arr[high] = arr[high],arr[pindex+1]
    
    return (i+1)
        
arr = [7,1,2,3,4,5,6]
n = len(arr)

AlternateSort(arr,n)
print(QuickSort(arr,0,n-1))