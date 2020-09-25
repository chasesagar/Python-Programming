''' Implement two stacks in an array 

create a data structure twostacks that represent two stacks. Implementation of twostalks
only use one array. 
i.e both stacks should only use the same array for sorting elements
function support:
Push
pop

 '''

# method one

class Twostacks:
    def __init__(self,size):
        self.arr = [None] * size
        self.mid = size // 2
        self.arr1 = 0
        self.arr2 = self.mid

    def Push1(self,data):
        if(self.arr1 < self.mid):
            self.arr[self.arr1] = data
            self.arr1 += 1
            print(self.arr)
        else:
            print("Stack1 is full \nno space to put", data)

    def Push2(self,data):
        if(self.arr2 >= self.mid and self.arr2 < len(self.arr)):
            self.arr[self.arr2] = data
            self.arr2 += 1
            print(self.arr)
        else:
            print("Stack2 is full \nno space to put", data)

    def Pop1(self):
        x = self.arr[self.arr1-1]
        self.arr.pop(self.arr1-1)
        self.arr1 -= 1
        return x

    def Pop2(self):
        x = self.arr[self.arr2-1]
        self.arr.pop(self.arr2-1)
        self.arr2 -= 1
        return x

# Driver
if (__name__=="__main__"):
    t = Twostacks(10)
    t.Push1(1)
    t.Push1(2)
    t.Push1(3)
    t.Push1(4)
    t.Push2(6)
    t.Push2(7)
    t.Push2(8)
    t.Push2(9)
    print(t.Pop2())
    print(t.Pop2())
    print(t.Pop2())
    print(t.Pop2())
    print(t.Pop1())

    



