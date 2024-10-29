# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:13:28 2024

@author: ahmed.a
"""

# Define the correct password
correct_password = "12345"
# Set the maximum number of attempts
max_attempts = 5
# Initialize the attempt counter
attempts = 0

while attempts < max_attempts:
    # Prompt the user for the password
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Access granted.")
        
    else:
        attempts += 1
        print(f"Incorrect password. Attempts remaining: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Maximum attempts reached. The authorities have been alerted.")
