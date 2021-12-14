# A sample python 3 rogram to transverse through a linked list

# code

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class contains a node object
class LinkedList:
    def __init__(self):
        self.head = None
 
    def push(self, new_data):
        """ Method to add node at starting position"""
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node

    def deleteNode(self, key):
        """Delete the first occurance of key from linked list"""
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return
        
        prev.next = temp.next
        temp = None


    def append(self, new_data):
        """ Method to append or add a new node at end"""
        new_node = Node(new_data)
        temp = self.head

        if self.head == None:
            self.head.next = new_node
            return

        while(temp.next):
            temp = temp.next

        temp.next = new_node

    def appendAfter(self, new_data, after):
        """ Method to add node after fiven position 4 1 2 3 5"""
        new_node = Node(new_data)
        temp = self.head

        if self.head == None:
            self.head.next = new_node
            return

        for i in range(0, after-1):
            temp = temp.next
        
        x = temp.next
        temp.next = new_node
        new_node.next = x

    def printList(self):
        """ Method to print content of linked list starting from head"""
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

# driver or code execution starts here
if __name__ == '__main__':
    # start with empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # link first node with second and so on
    llist.head.next = second
    second.next = third

    # print llist
    llist.printList()

    # Inserting a new node at first 
    llist.push(4)
    llist.printList()

    #Inserting a new node at end
    llist.append(5)
    llist.printList()

    # Insterting a new node after given vlaue
    llist.appendAfter(6, 3)
    llist.printList()

    # Delete node 
    llist.deleteNode(3)
    llist.printList()

