# code
"""def RearrangePosNev(arr,n):
    #initilazitation of temp array
    temp = []
    # copying original array into temp array
    for i in range(0,n):
        x = arr[i]
        temp.append(x)
    
    

    #sorting temp array
    temp.sort()
    print ("Sorted array is:", temp)
    # finding positive negative spearation point
    for i in range(0,n):
        if temp[i] >= 0 :
            negpos = i
            break

    j = negpos -1
    for i in range(1,n,2):
        arr[i] = temp[j]
        j = j-1
    
    j = negpos
    for i in range(0,n,2):
        arr[i] = temp[j]
        j = j+1

    return arr



#driver
arr = [-1,2,-3,4,5,6,-7,8,9]
n = len(arr)
RearrangePosNev(arr,n)

for i in range(0,n):
    print(arr[i], end= " ")"""

#code
def rearrange(arr,n):
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    pos, neg = i+1,0
    print(pos,neg)
    print(arr)

    while(pos<n and neg<pos and arr[neg]<0):
        arr[neg],arr[pos] = arr[pos],arr[neg]
        pos += 1
        neg += 2
    

def printarray(arr,n):
    for i in range(n):
        print(arr[i], end=" ")

# driver
arr = [-1,2,-3,4,5,6,-7,8,9]
n = len(arr)
rearrange(arr,n)
printarray(arr,n)