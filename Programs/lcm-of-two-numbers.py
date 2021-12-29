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

    def calculate_lcm_using_gcs(self):
        """
        A function provide lcm of two provide numbers
        using the GCF or GCD methos
        """
        lcm = int(int(self.n1 * self.n2) / int(self.calculate_gcd(self.n1, self.n2)))
        return lcm

    @staticmethod
    def calculate_gcd(n1, n2):
        """
        A static method to calculate GCD/GCF/HCF of given numbers
        """
        smaller = n1 if n2 > n1 else n2
        for i in range(1, smaller + 1):
            if n1 % i == 0 and n2 % i == 0:
                gcd = i
        return gcd

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
print(f"LCM of {n1} and {n2} using GCD method is {result.calculate_lcm_using_gcs()}")
