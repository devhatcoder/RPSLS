import pytest

from rpsls.backend import dataloader

@pytest.fixture
def ruleset():
    return dataloader.Ruleset()


def test_get_items(ruleset):
    expected = ['SCISSORS', 'PAPER', 'ROCK', 'LIZARD', 'SPOCK']
    actual = ruleset.get_items()
    assert actual == expected, "Items found in rules file does not match expected."

def test_get_winner(ruleset):
    assert ruleset.get_winner('SPOCK', 'SCISSORS') == 'SPOCK', "SPOCK must beat SCISSORS, logic failed."
    assert ruleset.get_winner('ROCK', 'PAPER') == 'PAPER', "PAPER must beat ROCK, logic failed."
    assert ruleset.get_winner('LIZARD', 'LIZARD') == False, "There shouldn't be any winner, logic failed."
