# A program to find factorial of a large number
import sys

class MathBasic:
    def __init__(self, num):
        self.num = num

    def calculate_factorial(self):
        """
            [A program to calculate factorial normal approach]
        """
        factorial = 1
        for i in range(1, self.num + 1):
            factorial = factorial * i

        print(f"Factorial of {self.num} is: {factorial}")

    def calculate_factorial_large_number(self):
        """
            [A program to calculate factorial using array storage approach]
            Time complexity: O(n)
            Space complexity: O(max) max = 500
        """
        res = [None for i in range(500)]

        res[0] = 1
        res_size = 1
        x = 2

        while x <= self.num:
            res_size = self.multiply(res, res_size, x)
            x = x + 1

        print("Factorial of given number is")
        i = res_size - 1
        while i >= 0:
            print(res[i], end="")
            # real function execution for print behind the scenes
            # sys.stdout.write(str(res[i]))
            #sys.stdout.flush()
            i = i - 1

    @staticmethod
    def multiply(res, res_size, x):
        carry = 0
        i = 0

        while i < res_size:
            prod = res[i] * x + carry
            res[i] = prod % 10
            carry = carry // 10
            i = i + 1

        while carry:
            res[res_size] = carry % 10
            carry = carry // 10
            res_size = res_size + 1

        return res_size


# Driver
res = MathBasic(100)
res.calculate_factorial()
res.calculate_factorial_large_number()
