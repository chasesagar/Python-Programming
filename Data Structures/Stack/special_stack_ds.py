''' 
Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() 
and an additional operation getMin() which should return minimum element from the SpecialStack. 
All these operations of SpecialStack must be O(1). 

example:

Consider the following SpecialStack
16  --> TOP
15
29
19
18

When getMin() is called it should 
return 15, which is the minimum 
element in the current stack. 

If we do pop two times on stack, 
the stack becomes
29  --> TOP
19
18

When getMin() is called, it should 
return 18 which is the minimum in 
the current stack.
'''
class Stack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def Push(self,data):
        self.s1.append(data)
        if(len(self.s2)==0):
            self.s2.append(data)
            global y
            y = data
        if(len(self.s2)!=0 and data < y):
            self.s2.append(data)
            y = data
        if(len(self.s2)!=0 and data > y):
            self.s2.append(y)

        return

    def pop(self):
        if(len(self.s1)== 0):
            print("Stack is empty")
            return
        x = self.s1[-1]
        self.s1.pop()
        return x

    def min(self):
        if(len(self.s1)== 0):
            print("Stack is empty, nothing to compare")
            return
        x = self.s2[-1]
        return x
# Driver code 
if __name__ == '__main__': 
	q = Stack() 
	q.Push(1) 
	q.Push(2) 
	q.Push(3)
	q.Push(4)
	q.Push(8)
	print(q.pop())
	print(q.pop())
	print(q.pop())
	print(q.min())

