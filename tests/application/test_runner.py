from application.runner import run_simulation
from domain.rectangular_grid import RectangularGrid
from domain.robot import Robot
from domain.position import Position
from domain.orientation import Orientation
from domain.command import Command

def test_run_simulation():
    grid = RectangularGrid(5, 5)
    
    robot1 = Robot(Position(1, 2), Orientation.NORTH)
    commands1 = [
        Command.LEFT, Command.MOVE, Command.LEFT, Command.MOVE,
        Command.LEFT, Command.MOVE, Command.LEFT, Command.MOVE, Command.MOVE
    ]
    
    robot2 = Robot(Position(3, 3), Orientation.EAST)
    commands2 = [
        Command.MOVE, Command.MOVE, Command.RIGHT, Command.MOVE, Command.MOVE, 
        Command.RIGHT, Command.MOVE, Command.RIGHT, Command.RIGHT, Command.MOVE
    ]
    
    result = run_simulation(grid, [
        (robot1, commands1),
        (robot2, commands2)
    ])
    
    assert result == ['1 3 N', '5 1 E']