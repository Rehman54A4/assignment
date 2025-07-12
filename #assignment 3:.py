#task1:
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive call
        return n * factorial(n - 1)

# Sample usage
sample_number = 5
result = factorial(sample_number)
print(f"The factorial of {sample_number} is: {result}")


#task2:
import math

# Asking the user for input
number = float(input("Enter a number: "))

# Calculations
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

# Displaying results
print(f"\nResults for the number {number}:")
print(f"Square root: {square_root}")
print(f"Natural logarithm (ln): {natural_log}")
print(f"Sine (in radians): {sine_value}")
