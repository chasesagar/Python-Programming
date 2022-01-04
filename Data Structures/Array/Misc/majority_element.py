""" 
A program to find majority element in given array arr, 
What is majority element? A 
majority element in an array A[] of size n is an element that appears more than n/2 times 
(and hence there is at most one such element).
"""


class ArrayBasic:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n

    def majority_element(self):
        """
        [A progrom to find majority element using hash map]
        Time Complexity = O(n)
        Auxiliary Space = O(n) Since a hashmap requires linear space.
        Returns:
            [str]: [A string with result info]
        """
        temp = {}
        for i in self.arr:
            temp[i] = 0 if temp.get(i) == None else temp[i] + 1

        for x, y in temp.items():
            if y >= self.n // 2:
                return f"Majority element is: {x}"

        return "No majority element"

    def majority_element_using_moore_voting_algo(self):
        """
        [A progrom to find majority element using moore voting algorithm]
        Time Complexity = O(n) As traversal of the array is needed, so the time complexity is linear.
        Auxiliary Space = O(1) As no extra space is required.
        Returns:
            [str]: [A string with result info]
        """
        mj_index = 0
        count = 1

        for i in range(self.n):
            count = count + 1 if self.arr[mj_index] == self.arr[i] else count - 1
            if count == 0:
                mj_index = i
                count = 1

        if self.arr.count(self.arr[mj_index]) >= self.n // 2:
            return f"Majority element is: {self.arr[mj_index]}"
        else:
            return "No majority element"

    def majority_element_using_sort(self):
        arr = self.arr.copy()
        # Sort time complexity O(nlogn)
        arr.sort()

        max_count = 0
        max_index = 0
        count = 0
        index = 0

        for i in range(self.n):

            if arr[index] == arr[i]:
                count += 1
            else:
                index = i
                count = 1

            if count > max_count:
                max_count = count
                max_index = arr[index]

        if max_count >= self.n // 2:
            return f"Majority element is: {max_index}"
        else:
            return "No majority element"


# Driver
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]

result = ArrayBasic(arr, len(arr))
print(result.majority_element())
print(result.majority_element_using_moore_voting_algo())
print(result.majority_element_using_sort())
