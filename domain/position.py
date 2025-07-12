from dataclasses import dataclass
from domain.orientation import Orientation

@dataclass(frozen=True)
class Position:
    x: int
    y: int
    
    def move(self, orientation: Orientation) -> 'Position':
        match orientation:
            case Orientation.NORTH:
                return Position(self.x, self.y + 1)
            case Orientation.EAST:
                return Position(self.x + 1, self.y)
            case Orientation.SOUTH:
                return Position(self.x, self.y - 1)
            case Orientation.WEST:
                return Position(self.x - 1, self.y)
            case _:
                raise ValueError(f'Invalid orientation: {orientation}')
    
    # I could create an alias if necessarry:
    def move_north(self) -> 'Position':
        self.move(Orientation.NORTH)