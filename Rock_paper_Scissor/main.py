import random

def get_choices():
    player_choice = input("Enter your choice(Rock,Paper,Scissor): ")
    options = ['Rock', 'Paper', 'Scissor']
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices

# choices = get_choices()
# print(choices)

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == 'Rock':
        if computer == 'Scissor':
            return "Rock smashes scissors! You won."
        else:
            return "Paper covers rock! You lose."
    elif player == 'Paper':
        if computer == 'Rock':
            return "Paper covers rock! You won."
        else:
            return "Scissor cuts paper! You lose."
    elif player == 'Scissor':
        if computer == 'Rock':
            return "Scissor smashes rock! You won."
        else:
            return "Paper covers rock! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)


