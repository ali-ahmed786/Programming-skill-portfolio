# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 18:52:48 2024

@author: ahmed.a
"""

# Dictionary of European countries and their capitals
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Portugal": "Lisbon",
    "Greece": "Athens"
}

# Loop through each country and ask for its capital
for country, capital in capitals.items():
    answer = input(f"What is the capital of {country}? ").strip().lower()
    if answer == capital.lower():
        print("Correct!")
    else:
        print("Incorrect.")
