# A program to find recuring sequence in a fraction


class BasicMath:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def fraction_to_decimal(self):
        res = ""
        rem = self.numerator % self.denominator
        mp = {}
        while (rem != 0) and (rem not in mp):
            # Append rem as key and it's occurrence in map array
            mp[rem] = len(res)
            # Multiply reminder by 10
            rem = rem * 10
            # Updating result after division
            res_part = rem // self.denominator
            res = res + str(res_part)

            # update reminder
            rem = rem % self.denominator

        if rem == 0:
            return f"{self.numerator // self.denominator}"
        else:
            return f"{self.numerator // self.denominator}.({res[mp[rem]:]})"


# Driver
# Driver code
s = BasicMath(50, 22)
res = s.fraction_to_decimal()
print("Fraction to decimal with recuring sequence is: ", res)

