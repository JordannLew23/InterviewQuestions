#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

#Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

#Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#Return k.

class Solution:
    # Define a class named Solution
    def removeDuplicates(self, nums: list[int]) -> int:
        # Define a method named 'removeDuplicates' that takes a list of integers called 'nums'
        # and returns an integer. The method is part of the Solution class.
        k = 1
        # Initialize a variable 'k' to 1. 'k' will keep track of the length of the unique elements.

        for i in range(1, len(nums)):
            # Begin a loop over the range of indices from 1 to the length of the 'nums' list.
            if nums[i] != nums[i-1]:
                # Check if the current element at index 'i' is different from the previous element.
                nums[k] = nums[i]
                # If they are different, update the element at index 'k' with the current element at index 'i'.
                k += 1
                # Increment 'k' by 1 to keep track of the length of unique elements.

        return k
        # Once the loop finishes, return the final value of 'k', which represents the number of unique elements.

# Create an instance of the Solution class
solution = Solution()

# Prompt the user for input and convert the input to a list of integers
nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Call the removeDuplicates method with the user-provided list of numbers
result = solution.removeDuplicates(nums)

# Print the result
print("Number of unique elements:", result)
