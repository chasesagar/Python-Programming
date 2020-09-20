''' 
Palindrome are those mumbers or words which read same from front and last.
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Push(self,new_data):
        if(self.head == None):
            self.head = Node(new_data)
        else:
            new_node = Node(new_data)
            new_node.next = None
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node

    def PrintList(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next
        print('')

    def CheckPalindrome(self): 
        arr = []
        temp = self.head
        while(temp != None):
            arr.append(temp.data)
            temp = temp.next
        temp = self.head
        while(temp != None):
            i = arr.pop()
            if(temp.data == i):
                ispal = True
            else:
                ispal = False
            temp = temp.next
        return ispal
#driver
if(__name__=="__main__"):
    list1 = LinkedList()
    values = [3,3,3] # R A D A R
    for i in values:
        list1.Push(i)
    list1.PrintList()
    print(list1.CheckPalindrome())
