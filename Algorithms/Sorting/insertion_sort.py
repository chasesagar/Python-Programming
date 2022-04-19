"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in 
your hands. The array is virtually split into a sorted and an unsorted part. Values from the 
unsorted part are picked and placed at the correct position in the sorted part.
"""

class Sort:
    def __init__(self, array: list):
        self.array = array
        self.length = len(array)

    def insertion_sort(self):
        """
        [A program to sort array using iterative insertion sort approach.]
        Time Complexity: O(N^2)
        Auxiliary space: O(1)
        Returns:
            List: Sorted array
        """
        # creating a copy of user input to avoid mutating the original array
        array = self.array.copy()
        # traversing through the array and inserting the element at the correct position
        for i in range(1, self.length):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array
    
    def recursive_insertion_sort(self, n=1):
        """
        [Recursive approach to sort array using insertion sort approach.]
        Time Complexity: O(N^2)
        Auxiliary space: O(1)
        Returns:
            List: Sorted array
        """
        if n == self.length:
            return self.array

        key = self.array[n]
        j = n - 1
        while j >= 0 and key < self.array[j]:
            self.array[j+1] = self.array[j]
            j -= 1
        self.array[j+1] = key

        return self.recursive_insertion_sort(n+1)

# driver code
def main():
    array = [12, 11, 13, 5, 6]
    sort = Sort(array)
    print(f"Iterative insertion sort is: {sort.insertion_sort()}")
    print(f"Recursive insertion sort is: {sort.recursive_insertion_sort()}")

if __name__ == "__main__":
    main()