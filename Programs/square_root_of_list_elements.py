# A program to calculate sqaure root of num_list elements


class Program:
    def __init__(self, num_list):
        self.num_list = num_list

    def calcualte_square_root(self):
        return [num * num for num in self.num_list]

    def calculate_sq_root_using_map(self):
        squares = list(map(lambda num: num ** 2, self.num_list))
        return squares


# Driver
num_list = [1, 2, 3, 4, 5]
result = Program(num_list)
print("Square root of given num_list {} is {}".format(num_list, result.calcualte_square_root()))
print("Square root of given num_list {} is {}".format(num_list, result.calculate_sq_root_using_map()))
