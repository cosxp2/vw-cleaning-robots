from domain.shape import WorkspaceShape
from domain.position import Position

class RectangularGrid(WorkspaceShape):
    def __init__(self, max_x: int, max_y:int):
        self.max_x = max_x
        self.max_y = max_y
        
    def is_valid_position(self, position: Position) -> bool:
        return (
            0 <= position.x <= self.max_x and
            0 <= position.y <= self.max_y
        )