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

    def PrintNthFromLast(self,k):
        temp = self.head
        n = 0
        while(temp !=None):
            temp = temp.next
            n +=1 #5
        
        if (k>n): # 2>5
            print("Location is greater than the length of the list")
            return
        
        temp = self.head
        for _ in range(0,n-k): # 0 to 5-2 = 3
            temp = temp.next
        print(temp.data)


#driver
if(__name__=="__main__"):
    list1 = LinkedList()
    values = [8,2,3,1,7] # 8 2 3 1 7
    for i in values:
        list1.Push(i)
    list1.PrintList()
    list1.PrintNthFromLast(2)