import random
from dict import author
from art import logo, vs

user_score = 0
user_input = []
winner = None

def game_choice():
    game = random.sample(list(author.keys()), 2)
    return game

def computer_compare(game):
    if author[game[0]] > author[game[1]]:
        return [game[0]]
    elif author[game[0]] < author[game[1]]:
        return [game[1]]
    else:
        return None

def compare():
    global user_score, winner
    if user_input == winner:
        user_score += 1 
        print(f"Your guess is correct. Your score is {user_score}.")
    else:
        user_score -= 1
        if user_score == 0:
            print(f"Your score is {user_score}. You lost.")
            
            return True
        else:
            print(f"Your score is {user_score}. Try again.")

    return False

def beginning_game():
    global user_input, winner, user_score
    while True:  
        game = game_choice()
        user_input = []
        choice_a, choice_b = game
        print(f"Compare A: {author[choice_a]}")
        print(vs)
        print(f"Against B: {author[choice_b]}")

        winner = computer_compare(game)

        user = input("\nWho has more books? Type 'A' or 'B' ").upper()
        if user == "A":
            user_input.append(choice_a)
        else:
            user_input.append(choice_b)

        if compare():
            break  

print(logo)
beginning_game()
