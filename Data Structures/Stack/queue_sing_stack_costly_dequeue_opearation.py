# Python3 programming to implement Queue using 
# two stack costly Dequeue operation
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self,data):
        #pushing element into stack s1
        self.s1.append(data)

    def deQueue(self):
        # checking if stack is empty
        if len(self.s1) == 0 :
            print("Stack is empty")
        # moving all elements from s1 to s2
        while(len(self.s1) != 0):
            self.s2.append(self.s1[-1])
            self.s1.pop()
        # popping out first element of s2
        x = self.s2[-1]
        self.s2.pop()
        # moving all elements from s2 to s1
        while(len(self.s2) != 0):
            self.s1.append(self.s2[-1])
            self.s2.pop()
        # returning value of poped element
        return x

# Driver code 
if __name__ == '__main__': 
	q = Queue() 
	q.enQueue(1) # push 1 in stack
	q.enQueue(2) # push 2 in stack
	q.enQueue(3) # push 3 in stack

	print(q.deQueue()) # remove 1 from stack like queue which is FIFO.
	print(q.deQueue()) 
	print(q.deQueue()) 



    