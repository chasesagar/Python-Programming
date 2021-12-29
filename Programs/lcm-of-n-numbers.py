# A program to find LCM of n numbers


class Program:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_lcm_using_brute_force(self):
        """
        In this method, the multiples of each number are listed until the first common multiple is found.
        """
        if not self.numbers or type(self.numbers) is int or len(self.numbers) < 2:
            return -1
        greater = self.numbers[0]
        lcm_found = 0

        for i in self.numbers:
            if i > greater:
                greater = i

        while True:
            for j in self.numbers:
                if greater % j == 0:
                    lcm_found += 1

            if lcm_found is len(self.numbers):
                break
            lcm_found = 0
            greater += 1

        return greater

    def calculate_lcm_using_gcd(self):
        """
        This method is used to find lcm of a list/tuple
        The formula used to find the LCM using the GCF or GCD is:
        L.C.M. = a×b/ gcd(a,b)
        """
        if not self.numbers or type(self.numbers) is int or len(self.numbers) < 2:
            return -1

        lcm = self.calculate_lcm_of_two_numbers(self.numbers[0], self.numbers[1])
        for i in range(2, len(self.numbers)):
            lcm = self.calculate_lcm_of_two_numbers(lcm, self.numbers[i])

        return lcm

    def calculate_lcm_of_two_numbers(self, n1, n2):
        """
        A utility function provide lcm of two provide numbers
        using the GCF or GCD methos
        """
        lcm = int(int(n1 * n2) / int(self.calculate_gcd(n1, n2)))
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


# driver
numbers = (22, 12, 35)

result = Program(numbers)
print(f"LCM of {numbers} using brute force approch is {result.calculate_lcm_using_brute_force()}")
print(f"LCM of {numbers} using GCD approch is {result.calculate_lcm_using_gcd()}")
