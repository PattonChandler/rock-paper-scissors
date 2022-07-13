import random
print("Welcome Player One to Rock, Paper, Scissors, Shoot!")
# USER INPUTS
user_choice = input("Please make a selection ('rock', 'paper', 'scissors'):")
user_choice = user_choice.lower()
print(f"You chose: '{user_choice}'")
# VALIDATE USER INPUTS
valid_options = ["rock", "paper", "scissors"]
if (user_choice not in valid_options):
    print("Not a valid option, please try again!")
    exit()
# COMPUTER CHOICE
computer_choice = random.choice(valid_options)
print("Computer choses:", computer_choice)
# DETERMINE THE WINNER
if user_choice == computer_choice:
    print("Tie! Please try again")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("You lose, sorry, try again!")
    else:
        print("You win and all of your dreams will come true!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("You lose, sorry, try again!")
    else:
        print("You win and all of your dreams will come true!")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("You lose, sorry, try again!")
    else:
        print("You win and all of your dreams will come true!")
# DISPLAY RESULTS
print("Thank you for playing, if you won, GREAT! If not, it might be time to consider another career path, a professional rock, paper, scissors player is not in the cards for you.")