#!/usr/bin/env python
import sys
import os

from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rpsls'))
import main_cli # noqa: E402
from backend import Ruleset # noqa: E402


@patch('builtins.input', return_value='scissors')
def test_get_input(input):
    assert main_cli.get_input() == 'SCISSORS', \
        "Output of get_input function does not match expected."


@patch('main_cli.get_input', return_value='ROCK')
def test_play(get_input, capsys):
    main_cli.play(Ruleset())
    std_out_err = capsys.readouterr()
    results = ['You win! Congratulations!!',
               'You lose! Better luck next time!!', 'No one wins!']
    assert any(text for text in results if text in std_out_err.out), \
        "The output does not contain any of the result strings."


@patch('builtins.input', return_value='q')
def test_main(input, capsys):
    try:
        main_cli.main()
    except SystemExit:
        pass
    std_out_err = capsys.readouterr()
    assert 'Thanks for playing! Goodbye!!' in std_out_err.out, \
        "Quitting message did not appear in output."
