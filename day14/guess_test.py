from unittest.mock import patch
import pytest
import random

from guess import Game, get_random_number

@patch.object(random, 'randint', return_value=10)
def test_get_random_number(m):
    assert get_random_number() == 10


@patch('builtins.input', side_effect=[11, '12', 'bob', 12, 5, -1, 21, 7, None])
def test_guess(inp):
    game = Game()
    # good
    assert game.guess() == 11
    assert game.guess() == 12
    # NaN with bob
    with pytest.raises(ValueError):
        game.guess()
    # Alredy has 12
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 5
    # Out of range with -1
    with pytest.raises(ValueError):
        game.guess()
    # Out of range with 21
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 7
    # NaN with None
    with pytest.raises(ValueError):
        game.guess()

def test_validation_guess(capfd):
    game = Game()
    game._answer = 2

    assert not game._validate_guess(1)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '1 is too low'

    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '3 is too high'

    assert game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '2 is correct!'

@patch('builtins.input', side_effect=[10, 22, 5, 6])
def test_game_win(inp, capfd):
    game = Game()
    game._answer = 6

    game()
    assert game._win is True

    out = capfd.readouterr()[0]
    expected = [
        '10 is too high',
        'Number not in range',
        '5 is too low',
        '6 is correct!',
        'It took you 3 guesses'
    ]

    output = [line.strip() for line in out.split('\n') if line.strip()]
    for line, exp in zip(output, expected):
        assert line == exp

@patch('builtins.input', side_effect=[1, 2, 3, 4, 5])
def test_game_lose(inp, capfd):
    game = Game()
    game._answer = 6

    game()
    assert game._win is False
    