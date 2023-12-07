import random
from dict import author
from art import logo, vs

game = []
user_input = []
winner = None  

def game_choice():
    choices = random.sample(list(author.keys()), 2)
    game.extend(choices)
    return choices

def computer_compare():
    global winner 
    if author[game[0]] > author[game[1]]:
        winner = [game[0]]
    elif author[game[0]] < author[game[1]]:
        winner = [game[1]]
    else:
        winner = []  
    return winner

def compare():
    if user_input == winner:
        print("Your guess is correct.")
    else:
        print("You lost.")

print(logo)
choice_a, choice_b = game_choice()
print(f"Compare A: {author[choice_a]}")
print(vs)
print(f"Against B: {author[choice_b]}")

computer_compare()

user = input("\nWho has more books? Type 'A' or 'B' ").upper()
if user == "A":
    user_input.append(choice_a)
else:
    user_input.append(choice_b)

compare()