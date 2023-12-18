#!/usr/bin/env python
from unittest.mock import patch

import rpsls.main
from rpsls.backend.dataloader import Ruleset

@patch('builtins.input', return_value='scissors')
def test_get_input(input):
    assert rpsls.main.get_input() == 'SCISSORS',\
        "Output of get_input function does not match expected."

@patch('rpsls.main.get_input', return_value='ROCK')
def test_play(get_input, capsys):
    rpsls.main.play(Ruleset())
    std_out_err = capsys.readouterr()
    results = ['You win! Congratulations!!',\
               'You lose! Better luck next time!!', 'No one wins!']
    assert any(text for text in results if text in std_out_err.out),\
        "The output does not contain any of the result strings."

@patch('builtins.input', return_value='q')
def test_main(input, capsys):
    try:
        rpsls.main.main()
    except SystemExit:
        pass
    std_out_err = capsys.readouterr()
    assert 'Thanks for playing! Goodbye!!' in std_out_err.out,\
        "Quitting message did not appear in output."
