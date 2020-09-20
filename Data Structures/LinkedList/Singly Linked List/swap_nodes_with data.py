#code
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Push(self,new_data):
        if(self.head)==None:
            self.head = Node(new_data)
        else:
            new_node = Node(new_data)
            new_node.next = None
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def PrintList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print('')

    def swapNodes(self, x, y): 
  
        # Nothing to do if x and y are same 
        if x == y: 
            return 
  
        # Search for x (keep track of prevX and CurrX) 
        prevX = None
        currX = self.head 
        while currX != None and currX.data != x: 
            prevX = currX 
            currX = currX.next
        print(prevX.data, "value if prevX")
        # Search for y (keep track of prevY and currY) 
        prevY = None
        currY = self.head 
        while currY != None and currY.data != y: 
            prevY = currY 
            currY = currY.next
        print(prevY.data, "value if prevy")
  
        # If either x or y is not present, nothing to do 
        if currX == None or currY == None: 
            return 
        # If x is not head of linked list 
        if prevX != None: 
            prevX.next = currY 
        else: #make y the new head 
            self.head = currY 
        print(prevX.data, "value if prevX after ")
        print(prevY.data, "value if prevY after ")
  
        # If y is not head of linked list 
        if prevY != None: 
            prevY.next = currX 
        else: # make x the new head 
            self.head = currX 
        print(prevX.data, "value if prevX after ")
        print(prevY.data, "value if prevY after ")
  
        # Swap next pointers 
        temp = currX.next
        currX.next = currY.next
        currY.next = temp 


#driver
if(__name__=="__main__"):
    list1 = LinkedList()
    values = [8,2,3,1,7] # 8 2 3 1 7
    for i in values:
        list1.Push(i)
    list1.PrintList()
    list1.swapNodes(2,7)
    list1.PrintList()