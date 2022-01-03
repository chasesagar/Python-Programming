def find_nth_natural_number(a, n):
    count = 1
    res = []
    while len(res) != n:
        if count % a != 0:
            res.append(count)
        count += 1

    return res[n-1]

def test():
    num = int(input())
    base = int(input("Base (2-9): "))
    if not(2 <= base <= 9):
        print(-1)

    newNum = ''

    while num > 0:
        newNum = str(num % base) + newNum
        num //= base

    print(newNum)

# Driver
print(find_nth_natural_number(9,12))
test()
