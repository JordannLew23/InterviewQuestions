#You are given three strings s1, s2, and s3. You have to perform the following operation on these three strings as many times as you want.
#In one operation you can choose one of these three strings such that its length is at least 2 and delete the rightmost character of it.
#Return the minimum number of operations you need to perform to make the three strings equal if there is a way to make them equal, otherwise, return -1.

# Define a class named Solution
class Solution:

    # Define a method named 'findMinimumOperations' that takes three strings 's1', 's2', and 's3'
    # and returns an integer representing the minimum number of operations required.
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:

        # Check if the first characters of 's1', 's2', and 's3' are equal
        if not (s1[0] == s2[0] == s3[0]):
            return -1  # Return -1 if the first characters are not equal

        # Initialize a variable 'k' to 0
        k = 0

        # Iterate over the characters of 's1', 's2', and 's3' using zip
        for c1, c2, c3 in zip(s1, s2, s3):

            # Break the loop if the characters are not equal
            if not (c1 == c2 == c3):
                break

            # Increment 'k' by 1
            k += 1

        # Calculate the minimum number of operations and return the result
        return len(s1) + len(s2) + len(s3) - k * 3
