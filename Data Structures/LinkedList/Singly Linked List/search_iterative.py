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
            while temp.next: # means temp.next != None
                temp = temp.next
            temp.next = new_node
    
    def PrintList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print('')
    # complete linked list deletition
    def DeleteLinkedList(self):
        temp = self.head
        while(temp):
            next = temp.next
            del temp.data
            temp = next
        print("Linked list deleted")
    
    # for searching a specifc element in linked list using Iterative approach
    def Search(self,k):
        temp = self.head
        while temp:
            if(temp.data==k):
                return True
            temp = temp.next
        return False

    #search program using recursion approach
    def RecSearch(self,li,k):
        if(li==None): # whenever next == None, linked list is finished and wee don`t find our key so it returns false
            return False
        if(li.data==k):
            return True
        
        return self.RecSearch(li.next,k)

    # for nth element
    def nth(self,k):
        temp = self.head
        for i in range(0,k-1):
            temp = temp.next

        x = temp.data
        return x

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = LinkedList()
        n = int(input()) #5
        values = list(map(int, input().strip().split())) # 8 2 3 1 7
        for i in values:
            list1.Push(i) # adding integers to linked list
        k = int(input()) #any works for all 
        list1.PrintList()
        if list1.Search(k): # driver for iterative approach
            print("Searched integer is present")
        else:
            print("Not present in given linked list")
        
        if list1.RecSearch(list1.head,k): # driver for recursion approach
            print("Searched integer is present")
        else:
            print("Not present in given linked list")

        print(list1.nth(k))
