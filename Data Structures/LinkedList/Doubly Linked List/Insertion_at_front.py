# Doubly Linked List


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Main insertion function
    def Push(self,new_data):
        new_node = Node(new_data)  # 1 & 2: Allocate the Node & Put in the data
        new_node.next = self.head  # 3. Make next of new node as head
        if self.head is not None:  # 4. change prev of head node to new node
            self.head.prev = new_node
        self.head = new_node        # 5. move the head to point to the new node
    
    # Print Function for double linked list.
    def PrintList(self):
        temp = self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp = temp.next
        print('')

#code
if(__name__=="__main__"):
    dlist = DoublyLinkedList()
    arr = [8,2,3,1,7]
    for i in arr:
        dlist.Push(i)
    dlist.PrintList()

