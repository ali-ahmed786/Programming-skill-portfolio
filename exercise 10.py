# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:16:38 2024

@author: ahmed.a
"""

def check_even_odd(number):
    """This function checks if the number is even or odd."""
    if number % 2 == 0:  # Check if the number is divisible by 2
        return "The number is even."  # Return message for even numbers
    else:
        return "The number is odd."   # Return message for odd numbers

def main():
    # Ask the user for a number
    user_input = input("Please enter a number: ")  # Get user input
    # Convert the input to an integer
    number = int(user_input)  

    # Call the function to check if the number is even or odd
    result = check_even_odd(number)

    # Print the result
    print(result)

# This condition checks if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function to start the program
