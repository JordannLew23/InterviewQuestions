# Define a class named Solution
class Solution:

    # Define a method named 'lengthOfLastWord' that takes a string 's'
    # and returns an integer representing the length of the last word.
    def lengthOfLastWord(self, s: str) -> int:

        # Initialize a variable 'length' to 0
        length = 0

        # Initialize a variable 'i' to the index of the last character in the string 's'
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count the length of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        # Return the final value of 'length'
        return length
