# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:48:21 2024

@author: ahmed.a
"""

# Store the information as key-value pairs in a dictionary
person_info = {
    "name": "John Doe",
    "hometown": "New York",
    "age": 25
}

print(f"Name: {person_info['name']}\nHometown: {person_info['hometown']}\nAge: {person_info['age']}")

# Get input from the user
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

# Ensure that the user enters a valid integer for age
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number for age.")

person_info = {
    "name": name,
    "hometown": hometown,
    "age": age}

# Print the values
print(f"Name: {person_info['name']}\nHometown: {person_info['hometown']}\nAge: {person_info['age']}")
