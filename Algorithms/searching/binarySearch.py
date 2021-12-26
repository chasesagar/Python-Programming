# code
def searchBinarySort(arr,H,K):
    L = 0
    while(L<=H):
        mid = (L + H) // 2
        if(arr[mid] == K):
            return 1
        elif(arr[mid]< K):
            L = mid + 1
        else:
            H = mid -1

    return -1



# driver
# if __name__ == '__main__':
#     t = int(input());
#     for _ in range(t):
#         NK = input().strip().split()
#         N = int(NK[0])
#         K = int(NK[1])
#         arr = [int(x) for x in input().strip().split()]
#         print(searchBinarySort(arr,N,K))

arr = [1,2,3,4,5,6,7]
N = len(arr)
K = 1
print(searchBinarySort(arr,N,K))