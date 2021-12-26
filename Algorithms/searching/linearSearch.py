#code
def linearSearch(arr,N,K):
    for i in range(len(arr)):
        if(arr[i] == K):
            return i + 1
    return -1





#driver
if(__name__ == '__main__'):
    t = int(input())
    for _ in range(t):
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        arr = [int(x) for x in input().strip().split()]

        print(linearSearch(arr,N,K))