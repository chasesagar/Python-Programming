# A program to find prime numbers in given range


class MathBasic:
    def __init__(self, start: int = 2, end: int = 10):
        self.start = start
        self.end = end
        self.recursion_prime_list = []

    def prime_numbers_list_compression(self):
        """
        [List compression approach]

        Returns:
            [list]: [A list of prime numbers will be returned]
        """
        primes = list(filter(lambda x: all(x % y != 0 for y in range(2, x)), range(self.start, self.end)))
        return primes

    def prime_numbers(self):
        """
        [Normal approach]

        Returns:
            [list]: [A list of prime numbers in given range will be returned]
        """
        primes = []
        for i in range(self.start, self.end):
            count = 0
            for j in range(2, i + 1):
                if i % j == 0:
                    count += 1
            if count == 1:
                primes.append(i)

        return primes

    def prime_numbers_recursion(self, num=2):
        """
        [Find prime number recursive approach]
        Args:
            num (int, optional): [description]. Defaults to 2.

        Returns:
            [list]: [A list of prime numbers in given range will be returned]
        """
        if num == self.end:
            return
        count = 0
        for i in range(2, num + 1):
            if num % i == 0:
                count += 1
        if count == 1:
            self.recursion_prime_list.append(num)
        self.prime_numbers_recursion(num + 1)

        return self.recursion_prime_list


# Driver
result = MathBasic()
print(f"List of prime numbers using is: {result.prime_numbers()}")
print(f"List of prime numbers using list compresion approach is: {result.prime_numbers_list_compression()}")
print(f"List of prime numbers using recursion approach is: {result.prime_numbers_recursion()}")
