#code
def copyList(head):
    curr = head
    while curr != None:
        new = Node(curr.data)
        new.next = curr.next
        curr.next = new
        curr = curr.next.next

    curr = head
    while curr != None:
        curr.next.random = curr.random

    curr = head
    dup = head.next
    while curr.next != None:
        temp = curr.next
        curr.next = curr.next.next
        curr = temp

    return dup

# driver
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
class LinkedList:
    def __init__(self):
        self.head = None

def insert(tail,data):
    tail.next=Node(data)
    return tail.next
    

def setarb(head,a,b):
    h=head
    i=1
    while i<a and h:
        h=h.next
        i+=1
    an=h
    
    h=head
    i=1
    while i<b and h:
        h=h.next
        i+=1
        
    if an:
        an.arb=h
        
def validation(head,res):
    
    while head and res:
        if id(head)==id(res):
            return
        
        #print(head.data,res.data,end=' ')
        if head.data != res.data:
            return
        
        if head.arb:
            if not res.arb:
                return
            
            #print(head.arb.data,res.arb.data)
            if head.arb.data != res.arb.data:
                return
            
        elif res.arb:
            return
        head=head.next
        res=res.next
        
    if not head and res:
        return
    elif head and not res:
        return
    
    return True


if __name__ == '__main__':
    nodes = [8,2,3,1,7]
    aarb = {{8,1},{1,3}}
    ll=LinkedList()
    ll.head=Node(nodes[0])
    tail=ll.head
        
    for x in nodes:
        tail=insert(tail,x)
           
    res=copyList(ll.head)
    
