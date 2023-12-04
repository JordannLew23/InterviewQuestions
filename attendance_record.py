#You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:


# Define a class named Solution
class Solution:

    # Define a method named 'checkRecord' that takes a string 's'
    # and returns a boolean indicating whether the attendance record is acceptable.
    def checkRecord(self, s: str) -> bool:

        # Initialize variables to count 'A's and consecutive 'L's
        count_A, count_L = 0, 0

        # Iterate over each character in the string 's'
        for c in s:
            # Check if the character is 'A'
            if c == 'A':
                # Increment the count of 'A's
                count_A += 1
                # Reset the count of consecutive 'L's
                count_L = 0
            # Check if the character is 'L'
            elif c == 'L':
                # Increment the count of consecutive 'L's
                count_L += 1
            else:
                # Reset the count of consecutive 'L's for other characters
                count_L = 0

            # Check if there are more than or equal to 2 'A's or more than or equal to 3 consecutive 'L's
            if count_A >= 2 or count_L >= 3:
                # If so, return False
                return False

        # If no conditions are violated, return True
        return True
