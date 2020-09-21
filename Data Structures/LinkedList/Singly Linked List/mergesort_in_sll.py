''' Merge sort of singly linked list
    Merge sort is often prefered for sorting a linked list. The slow random access performance 
    of linked list make other algorithms such as quicksort perform poorly and others such as 
    heapsort completely impossible. 
'''

#Code
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Push(self,new_data):
        if(self.head==None):
            self.head = Node(new_data)
        else:
            new_node = Node(new_data)
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node

    def PrintList(self): # function for printing linked list.
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
        print('')

    def MergeSort(self,h): # main Merge Sort function 
        if h is None or h.next is None :
            return h
        self.PrintList()
        middle = self.GetMiddle(h)
        nexttomiddle = middle.next
        middle.next = None

        left = self.MergeSort(h)
        right = self.MergeSort(nexttomiddle)

        sortedlist = self.SortedMerge(left,right)
        return sortedlist


    def GetMiddle(self,head): # function to get middle of linked list
        if (head == None):
            return head
        slow = fast = head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow

    def SortedMerge(self,a,b):
        result = None
        if a == None:
            return b
        if b == None:
            return a

        if (a.data <= b.data):
            result = a
            result.next = self.SortedMerge(a.next,b)
        else:
            result = b
            result.next = self.SortedMerge(a,b.next)
        
        return result


# Driver
if(__name__=="__main__"):
    list1 = LinkedList()
    values = [8,2,3,1,7] # 8 2 3 1 7
    for i in values:
        list1.Push(i)
    list1.PrintList()
    list1.head = list1.MergeSort(list1.head)
    list1.PrintList()
    
