#Descripiton
#You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.
#Return an array that consists of indices of peaks in the given array in any order.

# Define a class named Solution
class Solution:

    # Define a method named 'findPeaks' that takes a list of integers 'mountain'
    # and returns a list of indices where the elements form peaks in the mountain.
    def findPeaks(self, mountain: List[int]) -> List[int]:

        # Return a list comprehension that iterates over the enumerated zipped triplets
        # (a, b, c) of elements from the 'mountain' list.
        # For each triplet, if the middle element 'b' is greater than its neighbors 'a' and 'c',
        # add the index 'idx + 1' to the result list.
        return [idx + 1 for idx, (a, b, c) in enumerate(zip(mountain, mountain[1:], mountain[2:])) if a < b > c]
