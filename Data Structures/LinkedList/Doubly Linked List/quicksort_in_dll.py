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

    def QuickSort(self,low,high):
        pi = self.Partition(low,high)

        print(pi.prev.data)
        
        return self.QuickSort(low,pi)
        #self.QuickSort(pi.next,high)

    def Partition(self,low,high):
        pivot = high.data
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



class SortLinkedList:
    def __init__(self):
        return

    def quickSortUtil(self, head):
        pivot = head

        if head is None or head.next is None:
            return head, head, head

        head = head.next
        pivot.next = None

itr = head
prev = None
less_than_pivot = head
last_of_less_than_pivot = None

while itr is not None:
if itr.data < pivot.data:
if itr is less_than_pivot or prev is None:
last_of_less_than_pivot = less_than_pivot
else:
prev.next = itr.next
itr.next = less_than_pivot
less_than_pivot = itr
itr = prev

if last_of_less_than_pivot is None:
last_of_less_than_pivot = less_than_pivot

prev = itr
itr = itr.next

listA = less_than_pivot
listB = last_of_less_than_pivot.next
last_of_less_than_pivot.next = None

return listA, listB, pivot

def quickSort(self, head):
if head is not None and head.next is not None:

listA, listB, pivot = self.quickSortUtil(head)

listA = self.quickSort(listA)
listB = self.quickSort(listB)

temp = listA
while temp.next is not None:
temp = temp.next

temp.next = pivot
pivot.next = listB

return listA
else:
return head