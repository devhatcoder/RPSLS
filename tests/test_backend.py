import pytest

from rpsls.backend import Ruleset


@pytest.fixture
def ruleset():
    return Ruleset()


def test_get_items(ruleset):
    expected = ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']
    actual = ruleset.get_items()
    assert actual == expected, "Items found in rules file does not match expected."


def test_get_losers(ruleset):
    err_msg = "Incorrect data: Losers does not match expected."
    assert ruleset.get_losers('ROCK') == {'SCISSORS': 'Crushes', 'LIZARD': 'Crushes'}, err_msg
    assert ruleset.get_losers('PAPER') == {'ROCK': 'Covers', 'SPOCK': 'Disproves'}, err_msg
    assert ruleset.get_losers('SCISSORS') == {'PAPER': 'Cuts', 'LIZARD': 'Decapitates'}, err_msg
    assert ruleset.get_losers('LIZARD') == {'PAPER': 'Eats', 'SPOCK': 'Poisons'}, err_msg
    assert ruleset.get_losers('SPOCK') == {'SCISSORS': 'Smashes', 'ROCK': 'Vaporizes'}, err_msg


def test_get_winner(ruleset):
    assert ruleset.get_winner('SPOCK', 'SCISSORS') == ('SPOCK', 'Smashes', 'SCISSORS'), \
        "Logic failed: SPOCK must beat SCISSORS."
    assert ruleset.get_winner('ROCK', 'PAPER') == ('PAPER', 'Covers', 'ROCK'), "Logic failed: PAPER must beat ROCK."
    assert ruleset.get_winner('LIZARD', 'LIZARD') == (None, None, None), "Logic failed: There shouldn't be any winner."
