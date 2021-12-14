
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        if self.head == None:
            self.head =  Node(new_data)

        new_node = Node(new_data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
        print('')
