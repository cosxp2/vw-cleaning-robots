import pytest
from domain.command import Command

@pytest.mark.parametrize(
    ('input', 'expected'),
    [
        ('L', Command.LEFT),
        ('l', Command.LEFT),
        ('R', Command.RIGHT),
        ('r', Command.RIGHT),
        ('M', Command.MOVE),
        ('m', Command.MOVE)
    ]
)
def test_valid_command_input(input, expected):
    assert Command.from_str(input) == expected
    
@pytest.mark.parametrize(
    'input', ['X', '-1', '', '   ']
)
def test_invalid_command_input(input):
    with pytest.raises(ValueError):
        Command.from_str(input)