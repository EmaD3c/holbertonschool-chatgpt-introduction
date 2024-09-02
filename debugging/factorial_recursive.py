#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n recursively.

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input number n. If n is 0, the function returns 1,
         since 0! is defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the integer input from command-line arguments
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)
