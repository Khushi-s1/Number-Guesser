# -*- coding: utf-8 -*-
"""Number Guesser.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13B2C_svNOWlp_dX47OCp9LBIHUAAfV6o

Level-2 Task-2 Number Guesser

Create a number guessing game where the program generates a random number between a specified range, and the user tries to guess it.
"""

import random

def guess_number():
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)

    print(f"Guess the secret number between {lower_bound} and {upper_bound}")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))

            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
                continue

            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! {secret_number} is the correct number.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

guess_number()