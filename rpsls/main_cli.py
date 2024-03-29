#!/usr/bin/env python
'''
    This is the main script to run the game in CLI.
'''
from random import choice

from backend import Ruleset


def get_input(text=""):
    ''' Takes user input and pre-process before use. '''
    print('Type "Q" to quit the game.')
    print(text)
    user_in = input('Enter your choice: ').strip().upper()
    if user_in == "Q":
        print('Thanks for playing! Goodbye!!')
        quit()
    return user_in


def play(ruleset: Ruleset):
    ''' The complete steps for the gameplay. '''
    items = ruleset.get_items()
    player_item = get_input(f'Your options: {items}')
    while player_item not in items:
        print('Invalid choice, try again!')
        player_item = get_input(f'Your options: {items}')
    machine_item = choice(items)
    print(f'You choose: {player_item}, Machine choose: {machine_item}')
    winner, action, loser = ruleset.get_winner(player_item, machine_item)
    print()
    if winner == player_item:
        print(':D'*13)
        print('You win! Congratulations!!')
        print(':D'*13)
    elif winner == machine_item:
        print(':('*17)
        print('You lose! Better luck next time!!')
        print(':('*17)
    else:
        print(':|'*6)
        print('No one wins!')
        print(':|'*6)
    print()


def main():
    ruleset = Ruleset()
    print('Welcome to the game of "Rock Paper Scissors Lizar Spock!"')
    while True:
        play(ruleset)
        get_input('Want to play again? (Y)')


if __name__ == '__main__':
    main()
