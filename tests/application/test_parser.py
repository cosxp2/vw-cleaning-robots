import pytest
from application.parser import parse_input
from domain.rectangular_grid import RectangularGrid
from domain.robot import Robot
from domain.position import Position
from domain.orientation import Orientation
from domain.command import Command

def test_parse_input_single_robot():
    input_lines = [
        '5 5',
        '1 2 N',
        'LMLMLMLMM'
    ]

    grid, robot_instructions = parse_input(input_lines)

    assert isinstance(grid, RectangularGrid)
    assert grid.max_x == 5
    assert grid.max_y == 5

    assert len(robot_instructions) == 1

    robot, commands = robot_instructions[0]
    assert isinstance(robot, Robot)
    assert robot.position == Position(1, 2)
    assert robot.orientation == Orientation.NORTH

    assert commands == [
        Command.LEFT, Command.MOVE, Command.LEFT, Command.MOVE,
        Command.LEFT, Command.MOVE, Command.LEFT, Command.MOVE, Command.MOVE
    ]

def test_parse_input_multiple_robots():
    input_lines = [
        '5 5',
        '1 2 N',
        'LMLMLMLMM',
        '3 3 E',
        'MMRMMRMRRM'
    ]

    grid, robot_instructions = parse_input(input_lines)

    assert isinstance(grid, RectangularGrid)
    assert grid.max_x == 5
    assert grid.max_y == 5

    assert len(robot_instructions) == 2

    first_robot, first_commands = robot_instructions[0]
    second_robot, second_commands = robot_instructions[1]

    assert first_robot.position == Position(1, 2)
    assert first_robot.orientation == Orientation.NORTH
    assert first_commands == [
        Command.LEFT, Command.MOVE, Command.LEFT, Command.MOVE,
        Command.LEFT, Command.MOVE, Command.LEFT, Command.MOVE, Command.MOVE
    ]

    assert second_robot.position == Position(3, 3)
    assert second_robot.orientation == Orientation.EAST
    assert second_commands == [
        Command.MOVE, Command.MOVE, Command.RIGHT, Command.MOVE,
        Command.MOVE, Command.RIGHT, Command.MOVE, Command.RIGHT, Command.RIGHT, Command.MOVE
    ]

def test_parse_input_invalid_workspace():
    input_lines = [
        'invalid line',
        '1 2 N',
        'LMLMLMLMM'
    ]
    with pytest.raises(ValueError):
        parse_input(input_lines)

def test_parse_input_missing_command_line():
    input_lines = [
        '5 5',
        '1 2 N'
    ]
    with pytest.raises(ValueError):
        parse_input(input_lines)

def test_parse_input_blank_command_line():
    input_lines = [
        '5 5',
        '1 2 N',
        '',  
    ]
    _, robot_instructions = parse_input(input_lines)

    assert len(robot_instructions) == 1
    robot, commands = robot_instructions[0]
    assert robot.position == Position(1, 2)
    assert robot.orientation == Orientation.NORTH
    assert commands == []
    
def test_parse_input_empty():
    with pytest.raises(ValueError):
        parse_input([])