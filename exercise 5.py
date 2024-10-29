# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:10:36 2024

@author: ahmed.a
"""

# Dictionary with month numbers and corresponding days
days_in_month = {
    1: 31,  2: 28,  3: 31,
    4: 30,  5: 31,  6: 30,
    7: 31,  8: 31,  9: 30,
    10: 31, 11: 30, 12: 31
}

# Ask the user to enter a month number
month = int(input("Enter the month number (1-12): "))

# Check if the month is valid
if 1 <= month <= 12:
    # Special handling for February (leap year check)
    if month == 2:
        is_leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
        if is_leap_year == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        # Output the number of days for other months
        print(f"The month has {days_in_month[month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
