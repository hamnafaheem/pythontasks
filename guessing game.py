import random

def guess_the_number():
    lower_limit = 1
    upper_limit = 100
    number_to_guess = random.randint(lower_limit, upper_limit)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print(f"I'm thinking of a number between {lower_limit} and {upper_limit}.")

    while True:
        user_guess = input("Take a guess: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if user_guess < lower_limit or user_guess > upper_limit:
            print(f"Please guess a number between {lower_limit} and {upper_limit}.")
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()

