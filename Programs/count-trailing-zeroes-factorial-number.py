# A program to count trailing zero in factorial of the number
import functools


class MathBasic:
    def __init__(self, number):
        self.number = number

    def calculate_factorial(self):
        factorial = 1
        for i in range(1, self.number + 1):
            factorial = factorial * i
        return factorial

    def factorial_using_recursion(self, n):
        if n == 1:
            return 1
        else:
            return n * self.factorial_using_recursion(n - 1)

    def count_trailing_zero(self):
        fact = str(self.calculate_factorial())

        count = 0
        for i in range(1, len(fact)):
            if fact[-i] == "0":
                count += 1
            else:
                break
        return count

    def find_trailing_zeroes(self):
        if self.number < 0:
            return -1
        count = 0
        while self.number >= 5:
            self.number = self.number // 5
            count += 1

        return count


# Driver
s = MathBasic(7)
print(f"Factorial of the given number is: {s.calculate_factorial()}")
print(f"Factorial using recursion of the given number is: {s.factorial_using_recursion(7)}")
print(f"Trailing zeroes are: {s.count_trailing_zero()}")
print(f"Trailing zeroes using other approach is: {s.find_trailing_zeroes()}")
