# code
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

    def PrintList(self):
        temp = self.head
        if self.head is None:
            return
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print()

    def merge(self, first, second): 
        if first is None: 
            return second   
        if second is None: 
            return first 
  
        if first.data < second.data: 
            first.next = self.merge(first.next, second) 
            first.next.prev = first 
            first.prev = None   
            return first 
        else: 
            second.next = self.merge(first, second.next) 
            second.next.prev = second 
            second.prev = None
            return second 
   
    def mergeSort(self, temp): 
        if temp is None:  
            return temp 
        if temp.next is None: 
            return temp 
          
        second = self.split(temp) 
          
        temp = self.mergeSort(temp) 
        second = self.mergeSort(second) 
  
        return self.merge(temp, second) 
  
    def split(self, temp): 
        fast = slow =  temp 
        while(True): 
            if fast.next is None: 
                break
            if fast.next.next is None: 
                break
            fast = fast.next.next 
            slow = slow.next
              
        temp = slow.next
        slow.next = None
        return temp 

# driver

if(__name__=="__main__"):
    arr = [8,2,3,1,7]
    dlist = DoublyLinkedList()
    for i in arr:
        dlist.Push(i)
    dlist.PrintList()
    dlist.head = dlist.mergeSort(dlist.head)
    dlist.PrintList()
