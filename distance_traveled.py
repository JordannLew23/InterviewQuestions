#A truck has two fuel tanks. You are given two integers, mainTank representing the fuel present in the main tank in liters and additionalTank representing the fuel present in the additional tank in liters.

#The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank, if the additional tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the additional tank to the main tank.

#Return the maximum distance which can be traveled.



# Define a class named Solution
class Solution:

    # Define a method named distanceTraveled that takes two integer arguments: mainTank and additionalTank
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        # Initialize a variable 'res' to 0
        res = 0

        # While mainTank is greater than or equal to 5
        while mainTank >= 5:

            # Use divmod to calculate quotient and remainder of mainTank divided by 5
            quotient, remainder = divmod(mainTank, 5)

            # Add to 'res' the product of quotient, 5, and 10
            res += quotient * 5 * 10

            # Update mainTank to be the remainder plus the minimum of additionalTank and quotient
            mainTank = remainder + min(additionalTank, quotient)

            # Update additionalTank to be the maximum of additionalTank minus quotient and 0
            additionalTank = max(additionalTank - quotient, 0)

        # Add to 'res' the product of mainTank and 10
        res += mainTank * 10

        # Return the final value of 'res'
        return res

# Create an instance of the Solution class
solution = Solution()

# Prompt the user for input and convert the input to integers
mainTank = int(input("Enter the main tank value: "))
additionalTank = int(input("Enter the additional tank value: "))

# Call the distanceTraveled method with the user-provided values
result = solution.distanceTraveled(mainTank, additionalTank)

# Print the result
print("Total distance traveled in km:", result)
