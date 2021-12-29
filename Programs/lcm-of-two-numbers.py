# Program to find lcm of two numbers
import random

# using oop
class Program:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def compute_lcm(self):
        greater= self.n1 if self.n1 > self.n2 else self.n2

        while True:
            if (greater % self.n1 == 0) and (greater % self.n2 == 0):
                lcm = greater
                break
            greater += 1
        
        return lcm

def get_random_integer(start:int = 1, end:int= 100):
    """
        A utility function to generate random integers 
        in default range of 1 to 1000
    """
    return random.randint(start, end)

# driver
n1 = get_random_integer()
n2 = get_random_integer()

result = Program(n1, n2)
print(f"LCM of {n1} and {n2} is {result.compute_lcm()}")
