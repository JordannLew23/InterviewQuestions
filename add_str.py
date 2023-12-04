#Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

#You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.


# Define a class named Solution
class Solution:

    # Define a method named 'addStrings' that takes two strings 'num1' and 'num2'
    # representing non-negative integers and returns their sum as a string.
    def addStrings(self, num1: str, num2: str) -> str:

        # Convert 'num1' and 'num2' to integers and store them in variables 'n1' and 'n2'
        n1, n2 = int(num1), int(num2)

        # Calculate the sum of 'n1' and 'n2' and convert it to a string
        result = str(n1 + n2)

        # Return the result
        return result
