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

    def length(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp= temp.next
        
        return count

    def length_recursion(self, node, count=0):
        if node is None:
            return count

        return self.length_recursion(node.next, count+1)


    def nth_from_last_recursion(self, node, n, count = 0):
        
        if node is None:
            return

        if count == n:
            return node.data

        return self.nth_from_last_recursion(node.next, n, count + 1)


    def print_nth_from_last_recursion(self, n):
        len = self.length()
        if n > len:
            print(-1)
            return 
        print(self.nth_from_last_recursion(self.head, len-n))


#driver
if(__name__=="__main__"):
    list1 = LinkedList()
    values = [8,2,3,1,7] # 8 2 3 1 7
    for i in values:
        list1.Push(i)
    list1.PrintList()
    print(list1.length_recursion(list1.head))
    list1.PrintNthFromLast(2)
    list1.print_nth_from_last_recursion(2)