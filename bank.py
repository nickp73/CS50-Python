HELLO_GREET_REWARD = 0
H_GREET_REWARD = 20
OTHER_GREET_REWARD = 100

greeting = input("Greeting: ")

# .strip() removes accidental spaces at the start or end
processed_greeting = greeting.strip().capitalize()
# .capitalize() ensures the first letter is uppercase, and the rest are lowercase.

# Checks for "Hello" first (handles "Hello", "Hello, Name").
if processed_greeting.startswith("Hello"):
    reward = HELLO_GREET_REWARD
elif processed_greeting.startswith("H"):  # Checks for any other word starting with "H".
    reward = H_GREET_REWARD
else:                                    # Checks for everything else.
    reward = OTHER_GREET_REWARD

print(F"${reward}")