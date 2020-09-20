
#delet a linkd list at a given position

#code
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def printlist(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print('')

def delNode(head,position):
    position = position -1 # for considering real number delete means there is no number 0 our list start with 1 enale user to delete easily
    if(head==None):
        print("Linked List is empty, try pushing some data first")
        return
    
    temp = head #list1.head
    if(position==0):
        head = temp.next # list1.head = list1.head.next
        return head

    for i in range(position-1): # stop at (prev)-(prev)-(number need to delete)-(next) 8 2 3 1 5 hence if k = 4 it stops at 2
        print(i,temp)
        temp = temp.next # list1.head.next((8) --> (2,key) 
        print(temp)     # on next it will be temp.next(2,key)-->(3,key)
        if temp is None:
            break

    if temp is None:
        print("Position is out of range")
        return
    if temp.next is None:
        print("Position is out of range temp.next")
        return
    
    x = temp.next.next # pointing next of position to be deleted hence pointing next to the deleted value
    temp.next = None # setting prev of deleted to none
    temp.next = x # setting prev of deleted to next of deleted vlaue
    return head



# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input()) #5
        values = list(map(int, input().strip().split())) # 8 2 3 1 7
        for i in values:
            list1.insert(i)
        k = int(input()) #any works for all
        printlist(list1.head)
        newhead = delNode(list1.head, k)
        printlist(newhead)
