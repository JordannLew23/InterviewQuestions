# Define a class named Solution
class Solution:

    # Define a method named 'romanToInt' that takes a string 's' representing a Roman numeral
    # and returns an integer representing its corresponding decimal value.
    def romanToInt(self, s: str) -> int:

        # Create a dictionary 'm' mapping Roman numerals to their decimal values
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialize a variable 'ans' to 0
        ans = 0

        # Iterate over the characters of the input string 's'
        for i in range(len(s)):

            # Check if the current character is a subtractive numeral
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:

                # If so, subtract the current numeral's value from 'ans'
                ans -= m[s[i]]
            else:

                # Otherwise, add the current numeral's value to 'ans'
                ans += m[s[i]]

        # Return the final value of 'ans'
        return ans
