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
