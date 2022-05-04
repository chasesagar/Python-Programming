
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def costly_enqueue(self, data):
        """
        [Method to enqueue data]
        Time Complexity: O(N)
        Space complexity: O(N)
        Args:
            data : Data to be enqueued
        """
        while len(self.s1) != 0 :
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(data)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        """
        [Method to dequeue data]
        Time Complexity: O(1)
        Space complexity: O(N)
        """
        if len(self.s1) == 0:
            print("Queue is empty")
            return
        temp = self.s1[-1]
        self.s1.pop()

        return temp

    def enqueue(self, data):
        """
        [Method to enqueue data]
        Time Complexity: O(1)
        Space complexity: O(N)
        Args:
            data : Data to be enqueued
        """
        self.s1.append(data)

    def costly_dequeue(self):
        """
        [Dequeue using two stack costly Dequeue operation]
        Time Complexity: O(N)
        Space complexity: O(N)
        """
        if len(self.s1) == 0:
            print("Queue is empty")
            return
        
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        temp = self.s2[-1]
        self.s2.pop()

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

        return temp

# Driver code
if __name__ == '__main__':
    is_costly_enqueue = False
    q = Queue()

    if is_costly_enqueue:
        q.costly_enqueue(1)
        q.costly_enqueue(2)
        q.costly_enqueue(3)

        print(f"Queue is: {q.s1}")

        print(q.dequeue())
        print(q.dequeue())
        print(q.dequeue())

    else:
        q.enqueue(1) # push 1 in stack
        q.enqueue(2)
        q.enqueue(3)

        print(f"Queue is: {q.s1}")
        
        print(q.costly_dequeue()) # remove 1 from stack like queue which is FIFO.
        print(q.costly_dequeue())
        print(q.costly_dequeue())