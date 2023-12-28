#!/usr/bin/env python
'''
    Main script to run the game in GUI.
'''

from rpsls.frontend import AppGui
from rpsls.backend import Ruleset

def main():
    AppGui(Ruleset())

if __name__ == '__main__':
    main()
