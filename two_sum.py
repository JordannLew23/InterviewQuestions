# Define a class named Solution
class Solution:

    # Define a method named 'twoSum' that takes a list of integers 'nums' and an integer 'target'
    # and returns a list of two indices whose corresponding elements sum up to the target.
    def twoSum(self, nums):

        # Get the length of the 'nums' list and store it in variable 'n'
        n = len(nums)

        # Iterate over each index 'i' from 0 to n-2
        for i in range(n - 1):

            # Iterate over each index 'j' from i+1 to n-1
            for j in range(i + 1, n):

                # Check if the elements at indices 'i' and 'j' sum up to the target
                if nums[i] + nums[j] == target:

                    # If so, return a list containing the indices 'i' and 'j'
                    return [i, j]

        # If no solution is found, return None
        return None
