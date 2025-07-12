from domain.position import Position
from domain.orientation import Orientation
from domain.command import Command
from domain.shape import WorkspaceShape

class Robot():
    def __init__(self, position: Position, orientation: Orientation):
        self.position = position
        self.orientation = orientation     

    def turn_left(self) -> None:
        self.orientation = self.orientation.turn_left()
    
    def turn_right(self) -> None:
        self.orientation = self.orientation.turn_right()
    
    def move_forward(self, workspace: WorkspaceShape) -> None:
        next_position = self.position.move(self.orientation)
        if workspace.is_valid_position(next_position):
            self.position = next_position
        else:
            print('Desired position is outside workspace boundaries. \
                    Please provide a valid position')
    
    def execute(self, command: Command, workspace: WorkspaceShape) -> None:
        match command:
            case Command.LEFT:
                self.turn_left()
            case Command.RIGHT:
                self.turn_right()
            case Command.MOVE:
                self.move_forward()
            case _:
                raise ValueError(f'Invalid command: {command}')
            
    def __str__(self):
        return f'{self.position.x} {self.position.y} {self.orientation}'