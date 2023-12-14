'''
    This module deals with loading the data file,
    store rules and validates.
'''
import os

import yaml

class Ruleset():

    def __init__(self) -> None:
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                '..', 'data', 'rules.yml')
        with open(file_path, 'r') as rule_file:
            self.__rules = yaml.safe_load(rule_file)

    def get_items(self) -> list:
        '''
            Get the items from rule file.
        '''
        return list(self.__rules.keys())
    
    def get_losers(self, item_name: str) -> dict:
        '''
            Get the loser items as a dict which cannot beat the
            given item_name.
        '''
        try:
            return self.__rules[item_name.upper()]
        except KeyError:
            print(f'[ERROR] Invalid input: "{item_name}"')
            exit(1)

    def get_winner(self, player_item, machine_item):
        '''
            Get the winner from two choices.
        '''
        player_beats = self.get_losers(player_item)
        machine_beats = self.get_losers(machine_item)
        if machine_item in player_beats:
            print(f'{player_item} {player_beats[machine_item]} {machine_item}')
            return player_item
        elif player_item in machine_beats:
            print(f'{machine_item} {machine_beats[player_item]} {player_item}')
            return machine_item
        else:
            return False
