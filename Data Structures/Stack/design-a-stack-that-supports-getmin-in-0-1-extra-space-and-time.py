""" we already know solution for o(n) extra space now time to learn something new.
16  --> top
15
29
19
18
when getmin() called --> 15
pop() --> 16
pop() --> 15
getmin() --> 18

"""
#code

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Node({})".format(self.data)

class Stack :
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None

    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.data))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {}\n\n stack: \n{}'.format(self.top, out))

    def getmin(self):
        if self.top is None:
            return "Stack is empty."
        else:
            print("Minimum element in stack is: {}".format(self.minimum))

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    
    def Peek(self):
        if self.top is None:
            print("stack is empty.")
        else:
            if self.top.data < self.minimum:
                print("Top most element is: {}".format(self.minimum))
            else:
                print("Top most element is: {}".format(self.top.data))
                 
    def Push(self,data):
        if self.top is None:
            self.top = Node(data)
            self.minimum = data
        elif data < self.minimum:
            temp = (2 * data) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = data
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted is: {}".format(data))

    def Pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            removedNode = self.top.data
            self.top = self.top.next
            if removedNode < self.minimum:
                print("Top most element removed: {}".format(self.minimum))
                self.minimum = ((2* self.minimum)-removedNode)
            else:
                print("Top most element removed: {}".format(removedNode))

#driver 
stack = Stack()  
  
stack.Push(3) 
stack.Push(5)  
stack.getmin() 
stack.Push(2) 
stack.Push(1) 
stack.getmin()      
stack.Pop() 
stack.getmin() 
stack.Pop()  
stack.Peek() 
print(stack.__str__())