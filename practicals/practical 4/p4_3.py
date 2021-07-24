# guess the random number game

import random


def random_number_game():
    """
    This function generates a random number between 1 and 10,
    and asks the user to guess the number.
    """
    number = random.randint(1, 9)
    guess = int(input("Guess a number between 1 and 10: "))
    while guess != number:
        if guess < number:
            guess = int(input("Too low, guess again: "))
        elif guess > number:
            guess = int(input("Too high, guess again: "))
    print("You got it!")


if __name__ == "__main__":
    random_number_game()
