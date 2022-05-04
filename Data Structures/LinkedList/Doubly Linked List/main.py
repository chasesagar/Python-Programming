

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        return ""
            

    def push(self, new_data):
        """
        [Method to Add a node at the front: A 5 steps process]

        Args:
            new_data (): Data to be added into the linked list.
        """
        # 1. Allocate the node, and 2. put data in there
        new_node = Node(new_data)

        # 3. Make next of new_node as head and prev as null(default)
        new_node.next = self.head

        # 4. change prev of head node to new node
        if self.head is  not None:
            self.head.prev = new_node
        
        # 5. move the head to point to the new node
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        """
        [Method to Add a node after a given node A 7 steps process ]

        Args:
            prev_node (class Node): Prev node
            new_data (class Node): Data to be added into the linked list.
        """
        # 1. check if the given prev_node is NULL
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return

        # 2. Allocate the node, and 3. put data in there
        new_node = Node(new_data)
        # 4. Make next of new node as next of prev_node
        new_node.next = prev_node.next
        # 5. Make the next of prev_node as new_node
        prev_node.next = new_node
        # 6. Make prev_node as previous of new_node
        new_node.prev = prev_node
        # 7. Change previous of new_node's next node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def insert_before(self, next_node, new_data):
        """
        [Method to Add a node before a given node A 7 steps process ]

        Args:
            next_node (class Node): Node node
            new_data (class Node): Data to be added into the linked list.
        """
        if next_node is None:
            print("New node can be inserted before null")
            return

        new_node = Node(new_data)

        new_node.next = next_node
        new_node.prev = next_node.prev

        next_node.prev = new_node
        new_node.prev.next = new_node
    
    def append(self, new_data):
        """
        [Method to Add a node at the end od double linked list]

        Args:
            new_data (): Data to be added into the linked list.
        """
        new_node = Node(new_data)
        temp = self.head
        
        if self.head is None:
            self.head = new_node
            return
        
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp




# driver code
if __name__=="__main__":
    list = DoubleLinkedList()
    arr = [8,2,3,1,7]
    for i in arr:
        list.push(i)
    print(list)
    list.insert_after(list.head, 10)
    print(list)
    list.insert_before(list.head.next, 9)
    print(list)
    list.append(5)
    print(list)

         