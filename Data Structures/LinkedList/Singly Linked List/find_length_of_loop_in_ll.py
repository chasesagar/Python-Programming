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

    def PrintList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
        print('')

    def CreateLoop(self,n):
        Loopnode = self.head
        for _ in range(1,n):
            Loopnode = Loopnode.next
        
        temp = self.head
        while(temp.next):
            temp = temp.next

        temp.next = Loopnode

    def DetectLoop(self):
        s = []
        temp = self.head
        while(temp):
            if(temp in s):
                print("Loop is present")
                #for i in range(0,len(s)):
                    #if(s[i]==temp):
                i = s.index(temp)
                return print(len(s)-i)
                # for this our both of the methods work wether it is index method or for loop.   
                # gfg time exceeded error
                
            s.append(temp)
            temp = temp.next
        print("No Loop Is Present")
        '''
        temp = self.head
        fast = temp.next
        while(temp):
            while(fast): # this doesn't work because the loop is never going to end so it keeps on going ang going
                if(temp == fast):
                    print("Loop Found")
                    return 
                fast = fast.next
            temp = temp.next
            fast = temp.next
        print("No Loop Found")
        return
        '''
if(__name__=="__main__"):
    list1 = LinkedList()
    values = [8,2,3,1,7] # 8 2 3 1 7
    for i in values:
        list1.Push(i)
    list1.PrintList()
    list1.CreateLoop(0)
    list1.DetectLoop()
