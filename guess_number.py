#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: oct 2022
# This program guess the random number

import random

random_number = random.randint(0, 9)  # a number between 0 and 9


def main():
    # this function guess the random number

    # input
    guess = int(input("Enter a number between 0 and 9: "))
    print("")

    # process & output
    if guess == random_number:
        print("Congratulations, you guessed correct!")
    else:
        print("Sorry, you guessed wrong!")

    print("\nDone.")


if __name__ == "__main__":
    main()
