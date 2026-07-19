WORDS = {"PAIR": 4, "HAIR": 4, "BEAR": 4, "BARE": 4, "TEAR": 4, "RATE": 4, "EAT": 3, "ATE": 3, "TEA": 3, "EAR": 3, "ARE": 3, "ART": 3, "RAT": 3, "TAR": 3, "BAT": 3, "TAB": 3, "BAR": 3, "BRA": 3}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")


    while len(WORDS) > 0:
        print(f"\nYou have {len(WORDS)} words left to guess.")
        guess = input("Enter a word (or 'quit' to exit): ").upper()

        if guess == "QUIT":
            break
        if guess == "GRAPHIC":
            WORDS.clear()
            print("Congratulations! You've guessed the secret word and completed the game!")


        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Correct! '{guess}' You scored {points} points.")
        else:
            print(f"Sorry, '{guess}' is not a valid word.")

    print("\nThanks for playing!")

"""
def main():
    print("Welcome to Spelling Bee!")
    for key, points in WORDS.items():
        print(f"{key} was worth {points} points.")
"""

if __name__ == "__main__":
    main()