"""
Heap sort is a comparison-based sorting technique based on Binary Heap data structure. 
It is similar to selection sort where we first find the minimum element and place the 
minimum element at the beginning. We repeat the same process for the remaining elements.

Heap Sort Algorithm for sorting in increasing order: 
1. Build a max heap from the input data. 
2. At this point, the largest item is stored at the root of the heap. Replace it with the 
last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of the tree. 
3. Repeat step 2 while the size of the heap is greater than 1.

"""
class Sort:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def heap_sort(self):
        """
        [Heap sort function]
        Time complexity: O(NlogN)
        """
        # Build a maxheap.
        for i in range(self.length//2 - 1, -1, -1):
            self.heapify(self.arr, self.length, i)
 
        # One by one extract elements
        for i in range(self.length-1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i] 
            self.heapify(self.arr, i, 0)
    
    def heapify(self, arr, size, index):
        """
        [The process of reshaping a binary tree into a Heap data structure is known as heapify.]
        Time complexity: O(Logn)
        Args:
            arr (list): User input array which needed to be heapified
            size (int): Size or maximum possible height of heap
            index (int): Root index
        """
        largest = index # Initialize largest as root
        left_node = 2 * index + 1
        right_node = 2 * index + 2

        if left_node < size and arr[largest] < arr[left_node]:
            largest = left_node
        
        if right_node < size and arr[largest] < arr[right_node]:
            largest = right_node

        if largest != index:
            arr[largest], arr[index] = arr[index], arr[largest]

            self.heapify(arr, size, largest)

# Driver code
arr = [12, 11, 13, 5, 6, 7]
sort = Sort(arr)
sort.heap_sort()
print(f"Sorted array is: {sort.arr}")

