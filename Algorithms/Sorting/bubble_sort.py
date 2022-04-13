"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the 
adjacent elements if they are in wrong order
"""

class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def __str__(self):
        return " ".join([str(x) for x in self.arr])

    def bubble_sort(self):
        """
        [A program to sort array using iterative bubble sort approach.]
        Time Complexity: O(N^2)
        Auxiliary space: O(1)
        Returns:
            List: Sorted array
        """
        arr = self.arr.copy()
        length = self.length

        for i in range(length):
            swapped = False
            for j in range(length-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    def recursive_bubble_sort(self, n = None):
        """
        [Recursive program to sort array using bubble sort approach.]
        Time Complexity: O(N^2)
        Auxiliary space: O(1)
        Returns:
            List: Sorted array
        """
        if n is None:
            n = self.length
        # base condition 
        if n == 1:
            return self.arr
        
        for i in range(n-1):
            if self.arr[i] > self.arr[i+1]:
                self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]

        return self.recursive_bubble_sort(n-1)

    def recursive_bubble_sort_second(self, arr):
        """
        [Recursieve approach to sort array using bubble sort approach.]
        Time Complexity: O(N^2)
        Auxiliary space: O(1)
        Returns:
            List: Sorted array
        """
        if len(arr) == 1:
            return arr
    
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        return self.recursive_bubble_sort_second(arr[:-1]) + [arr[-1]]

# Driver code
def main():
    array = [64, 34, 25, 12, 22, 11, 90]
    sort = BubbleSort(array)
    # Sorting array
    print(f"Bubble sorted array is: {sort.bubble_sort()}")
    print(f"Recursive bubble sorted array is: {sort.recursive_bubble_sort_second(array)}")
    print(f"Recursive bubble sorted array second approach is: {sort.recursive_bubble_sort()}")
 

if __name__ == "__main__":
    main()