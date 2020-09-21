''' Status
    Still Uncomplete 
'''

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

    def gethighestnode(self):
        temp = self.head

        while temp.next is not None:
            temp = temp.next
        print(temp.data)
        return temp

    def Lowestnode(self):
        temp = self.head
        print(temp.data)
        return temp
    #uncomplete 
    def QuickSort(self,low,high):
        pi = self.Partition(low,high) # works 

        print(pi.prev.data) # works, just for debugging purpose
        
        self.QuickSort(low,pi) # Not working end up having an infinite loop.
        self.QuickSort(pi.next,high) #  commenting this section give problem in partition section > pivot for upper call.

    def Partition(self,low,high):
        pivot = high.data # error high.data has no variable called Data.
        pindex = low
        temp = low

        while temp.next is not None:
            if temp.data < pivot:
                temp.data,pindex.data = pindex.data,temp.data
                pindex = pindex.next
            temp = temp.next
        pindex.data,high.data = high.data,pindex.data

        return pindex
    
# driver
if(__name__=="__main__"):
    arr = [8,2,3,1,7]
    dlist = DoublyLinkedList()
    for i in arr:
        dlist.Push(i)
    dlist.PrintList()
    low = dlist.Lowestnode()
    high = dlist.gethighestnode()
    dlist.QuickSort(low,high)
    dlist.PrintList()