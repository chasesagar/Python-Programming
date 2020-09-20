#code
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = None

    def Push(self,new_data):
        if(self.head== None):
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
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print('')

    def DeleteLinkedList(self):
        temp = self.head
        while(temp):
            next = temp.next
            del temp.data
            temp = next
        print("Linked list deleted")

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = LinkedList()
        n = int(input()) #5
        values = list(map(int, input().strip().split())) # 8 2 3 1 7
        for i in values:
            list1.Push(i)
        k = int(input()) #any works for all
        list1.PrintList()
        list1.DeleteLinkedList()

    
