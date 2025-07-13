import pytest
from application.runner import run_simulation
from domain.rectangular_grid import RectangularGrid
from domain.robot import Robot
from domain.position import Position
from domain.orientation import Orientation
from domain.command import Command

@pytest.fixture(scope='module')
def grid():
    return RectangularGrid(5, 5)

def test_run_simulation_no_overlapping(grid):    
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


def test_run_simulation_robots_overlapping(grid, capfd):
    # robot1 moves forward into (1, 3)
    robot1 = Robot(Position(1, 2), Orientation.NORTH)
    commands1 = [Command.MOVE]

    # robot2 tries to move into the same cell (1, 3)
    robot2 = Robot(Position(1, 2), Orientation.NORTH)
    commands2 = [Command.MOVE]  # 2nd move is skipped

    results = run_simulation(grid, [
        (robot1, commands1),
        (robot2, commands2)
    ])

    assert results[0] == '1 3 N'
    assert results[1] == '1 2 N'  # second move was skipped due to occupancy

    out, _ = capfd.readouterr()
    assert 'Blocked: Position(x=1, y=3) is already occupied' in out
