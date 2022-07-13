import random
print("Rock, Paper, Scissors, Shoot!")
# USER INPUTS
user_choice = input("Please make a selection ('rock', 'paper', 'scissors'):")
print(f"You chose: '{user_choice}'")
# VALIDATE USER INPUTS

# COMPUTER CHOICE
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)
# DETERMINE THE WINNER

# DISPLAY RESULTS