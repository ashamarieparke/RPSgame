#rpsgame.py
#December 20,2021
#Program allows the user to play rock paper scissors with the computer
import random
def start():
    print('Rock Paper Scissors Game...')
    print('Choose one of the following:')
    print('r - rock')
    print('p - paper')
    print('s - scissors')
    user = input("What's your choice:")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'Tied game!'
    #r > s , s > p , p > r
    if is_win(user,computer):
        return 'You won!'

    return 'You lost!'


    
    
def is_win(player,opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True #return True if player wins
               
    
    

    
    

 
    
    
