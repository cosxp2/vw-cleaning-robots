from __future__ import annotations
from enum import Enum

class Orientation(Enum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'
    
    @classmethod
    def _clockwise(cls) -> list[Orientation]:
        return [cls.NORTH, cls.EAST, cls.SOUTH, cls.WEST]
    
    def turn_left(self) -> Orientation:
        directions = self._clockwise()
        idx = directions.index(self)
        return directions[(idx - 1) % len(directions)]

    def turn_right(self) -> Orientation:
        directions = self._clockwise()
        idx = directions.index(self)
        return directions[(idx + 1) % len(directions)]
    
    def __str__(self) -> str:
        return self.value
    
    @staticmethod
    def from_str(value: str) -> Orientation:
        try:
            return Orientation(value.upper())
        except ValueError:
            raise ValueError(f'Invalid orientation: {value}')