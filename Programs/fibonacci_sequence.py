# A program to print fibonacci sequence

class BasicMath:
    def __init__(self,length=10):
        self.length = length
        self.fib = [0,1]

    def fibonacci_sequence(self):
        fib= [0,1]
        [fib.append(fib[-2]+fib[-1]) for i in range(self.length-2)]
        print("Fibonacci sequence using loop is: ",fib)

    def fibonacci_recursion(self):
        if len(self.fib) == self.length:
            print("Fibonacci sequence using recursion is: ",self.fib)
            return
        self.fib.append(self.fib[-2]+self.fib[-1])
        self.fibonacci_recursion()

# Driver
result = BasicMath()
result.fibonacci_sequence()
result.fibonacci_recursion()