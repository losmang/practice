import random

def play():
    user = input("Choose one: 'r' for Rock , 'p' for Paper , 's' for Scissors: ")
    computer = random.choice(['r', 'p' , 's'])

    if user == computer:
        return 'It\'s a Tie'

    if is_win(user , computer):
        return 'You Won!'

    return 'You Lost! :('

    # r > s , s > p , p > r

def is_win(player , opponent):
    #return true if player wins
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(play())
