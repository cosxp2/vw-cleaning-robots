from __future__ import annotations
from enum import Enum

class Command(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    MOVE = 'M'
    
    @staticmethod
    def from_str(value: str) -> Command:
        try:
            return Command(value.upper())
        except ValueError:
            raise ValueError(f'Invalid command: {value}')