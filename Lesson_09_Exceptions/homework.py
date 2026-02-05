# Homework: Exceptions

# 1. Write a function that divides two numbers. Handle the ZeroDivisionError if the denominator is 0.
def safe_divide(a, b):
    # Your code here
    pass

# Test cases:
# print(safe_divide(10, 2))  # Should print 5.0
# print(safe_divide(10, 0))  # Should print an error message, not crash

# 2. Write code that asks for user input and tries to convert it to an integer.
#    Handle the ValueError if the input is not a number.
user_input = "not_a_number"  # Simulating user input
# Your code here

# 3. Use a try-except-finally block.
#    - Try to open a file that doesn't exist.
#    - Catch the FileNotFoundError.
#    - In the finally block, print "Execution completed."
# Your code here

# 4. Raise a custom exception (ValueError) if a user's age is negative.
age = -5
# Your code here
