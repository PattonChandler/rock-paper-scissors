import random
print("Rock, Paper, Scissors, Shoot!")
# USER INPUTS
user_choice = input("Please make a selection ('rock', 'paper', 'scissors'):")
user_choice = user_choice.lower()
print(f"You chose: '{user_choice}'")
# VALIDATE USER INPUTS
valid_options = ["rock", "paper", "scissors"]
if (user_choice not in valid_options):
    print("Not a valid option, please try again")
    exit()
# COMPUTER CHOICE
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)
# DETERMINE THE WINNER

# DISPLAY RESULTS