from domain.rectangular_grid import RectangularGrid
from domain.robot import Robot
from domain.command import Command

def run_simulation(grid: RectangularGrid, robot_info: list[tuple[Robot, list[Command]]]) -> list[str]:
    final_states = []
    
    for robot, commands in robot_info:
        robot.execute_all(commands, grid)
        final_states.append(str(robot))
    
    return final_states