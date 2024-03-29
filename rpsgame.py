#rpsgame.py

import random
import math

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # return true is the player beats the opponent
    # won if: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # tie
        if result == 0:
            print('It is a tie. You and the computer have both chosen {}. \n'.format(user))
        # if you win
        elif result == 1:
            player_wins += 1
            print('You won! Congrats! You chose {} and the computer chose {}.\n'.format(user, computer))
        
        #if you lose
        else:
            computer_wins += 1
            print('Sadly, you lost :(. You chose {} and the computer chose {}.\n'.format(user, computer))

    if player_wins > computer_wins:
        print('Yippee! You have been declared winner! :D You have won the best of {} games!'.format(n))
    else:
        print('Unfortunately, you lost :(! The computer has won the best of {} games. Better luck next time!'.format(n))


if __name__ == '__main__':
    play_best_of(3)
