#code

def leftRotateByOne(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def rotateArray(arr, n , d):
    for i in range(d):
        leftRotateByOne(arr,n)
        
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# driver
if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        #take n and d as input
        n_d = [int(x) for x in input().strip().split()]
        n = n_d[0]
        d = n_d[1]
        arr = [int(x) for x in input().strip().split()]
        
        rotateArray(arr, n, d)
        printArray(arr, n)
        t = t - 1;
        