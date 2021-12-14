
# code
def iterate(list, start, end):
    if start < 0 or end > len(list) or start >= end:
        return 
    print(list[start], end=' ')
    iterate(list, start + 1, end)

# driver

arr = [1,2,3,4,5,6,7,8,9,10]

iterate(arr, 0, len(arr))