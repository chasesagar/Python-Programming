
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class MiddleStack:
    """
    [Stack with operations on middle element with O(1) time complexity]
    """
    def __init__(self):
        self.head = None
        self.middle = None
        self.count = 0

    def __str__(self):
        print("Stack is:", end=" ")
        temp = self.head
        if temp is None:
            print("underflow")
            return ""
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        return ""

    def push(self,new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.count += 1

        if self.count == 1:
            self.middle = new_node
        else:
            self.head.prev = new_node
            if self.count % 2 != 0:
                self.middle = self.middle.prev
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack underflow")
            return
        temp = self.head.data
        self.head = self.head.next
        self.head.prev = None
        self.count -= 1

        if self.count % 2 == 0:
            self.middle = self.middle.next

        return temp

    def get_middle(self):
        if self.head is None:
            print("Stack underflow")
            return
        return self.middle.data




# Driver code
if __name__ == '__main__':
 
    s = MiddleStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    print(s)
    print(f"Stack middle element is: {s.get_middle()}")
    s.pop()
    print(s)
    print(f"Stack middle element is: {s.get_middle()}")

            