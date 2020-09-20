#code
def partition(arr,low,high):
    pivot = arr[high]
    pindex = low-1

    for i in range(low,high):
        if(arr[i]<pivot):
            pindex = pindex + 1
            arr[i],arr[pindex] = arr[pindex],arr[i]
        
    arr[pindex+1],arr[high] = arr[high],arr[pindex+1]
    
    return (i+1)

def QuickSort(arr,low,high):
    if( low < high):

        pi = partition(arr,low,high)

        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)

#driver
arr = [3,51,6,0,2,9,1,7,8,12,89,34,23,6]
n = len(arr)
QuickSort(arr,0,n-1)

for i in range(n):
    print(arr[i], end=" ")