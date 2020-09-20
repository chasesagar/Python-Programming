#code

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def Push(self,new_data):
        temp = self.head
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def PrintDList(self):
        temp = self.head
        if self.head is None:
            return
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print()

    def ReversePrint(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        rev = temp
        while rev is not None:
            print(rev.data,end=" ")
            rev = rev.prev
        print()
    
    def reverse(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev
        

if  (__name__ == "__main__"):
    arr = [8,2,3,1,7]
    dlist = DoublyLinkedList()
    for i in arr :
        dlist.Push(i)
    dlist.PrintDList()
    dlist.ReversePrint()
    dlist.reverse()
    dlist.PrintDList()
        
