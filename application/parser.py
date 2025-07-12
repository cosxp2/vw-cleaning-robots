from typing import Iterable
from domain.rectangular_grid import RectangularGrid
from domain.robot import Robot
from domain.position import Position 
from domain.orientation import Orientation
from domain.command import Command

def parse_workspace(line: str) -> RectangularGrid:
    try:
        x_str, y_str = line.strip().split()
        return RectangularGrid(int(x_str), int(y_str))
    except ValueError:
        raise ValueError(f'Invalid workspace definition: {line}')

def parse_robot(line: str) -> Robot:
    try: 
        x_str, y_str, orientation_str = line.strip().split()
        position = Position(int(x_str), int(y_str))
        orientation = Orientation.from_str(orientation_str)
        return Robot(position, orientation)
    except ValueError:
        raise ValueError(f'Invalid robot position definition: {line}')

def parse_commands(line: str) -> list[Command]:
    return [Command.from_str(char) for char in line.strip()]


def parse_input(lines: Iterable[str]) -> tuple[RectangularGrid, list[tuple[Robot, list[Command]]]]:
    lines = iter(lines)
    try:
        grid = parse_workspace(next(lines))
    except StopIteration:
        raise ValueError("No workspace line provided")

    robot_instructions = []

    while True:
        try:
            robot_line = next(lines).strip()
        except StopIteration:
            break  # no more input

        if not robot_line:
            continue  # skip blank lines

        try:
            command_line = next(lines).strip()
        except StopIteration:
            raise ValueError(f"Missing command line for robot at position: {robot_line}")

        robot = parse_robot(robot_line)
        commands = parse_commands(command_line)

        robot_instructions.append((robot, commands))

    return grid, robot_instructions