#code
def InsertionSort(arr,n):
    #transverse through whole array
    for i in range(1,n):
        key = arr[i]
        j = i-1
        # and this while loop keep sorting the delected elements.
        while(j>=0 and key<arr[j]):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

#driver
arr = [5,2,7,9,4,6,2,1,0]
n = len(arr)
InsertionSort(arr,n)
for i in range(0,n):
    print(arr[i], end = " ")
