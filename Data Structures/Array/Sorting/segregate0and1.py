#sort an array containing two types of elements.
""" 
We are given an array of 0s and 1s in random order.Segregate 0s to the left side 
and 1s to the right side of the array in only one transverse.
"""

def Segregate0and1(arr,n):
    index0 = 0
    index1 = n-1

    while(index0<index1):
        if(arr[index0]==1) and (arr[index1]==0):
            arr[index0],arr[index1] = arr[index1],arr[index0]
            index0 +=1
            index1 -=1
        if(arr[index0]==1) and (arr[index1]==1):
            index1 -=1
        if(arr[index0]==0):
            index0 +=1
#another approach

def segregate0and1(arr, n): 
  
    type0 = 0;
    type1 = n - 1
  
    while (type0 < type1):  
        if (arr[type0] == 1):  
            arr[type0], arr[type1] = arr[type1], arr[type0] 
            type1 -= 1
          
        else:  
            type0 += 1

if(__name__ == "__main__"):
    arr = [1,0, 1, 0, 1, 0, 0, 1, 1, 1, 0,1]
    n = len(arr)
    Segregate0and1(arr,n)
    for i in range(n):
        print(arr[i], end=" ")
    print()

