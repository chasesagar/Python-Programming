'''
    Remove duplicates from an unsorted linked list
    Write a removeDuplicates() function which takes a list and deletes any duplicate nodes from the list. 
    The list is not sorted. 
    
    For example if the linked list is 
    12->11->12->21->41->43->21 then removeDuplicates() should convert the list to 
    12->11->21->41->43. 

'''
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

    def RemoveDuplicates(self):
        temp = self.head

        while (temp !=None):
            print(temp.data)
            fast = temp.next
            s = temp
            print(s.data)
            while (fast != None):
                if(temp.data == fast.data):
                    new = fast.next
                    s.next = None
                    s.next = new 
                s = fast
                fast = fast.next
            temp = temp.next
    
        
        return 


if(__name__=="__main__"):
    list1 = LinkedList()
    values = [1,1,1,1,1,1] # 8 2 3 1 7
    for i in values:
        list1.Push(i)
    list1.PrintList()
    list1.RemoveDuplicates()
    list1.PrintList()
