from domain.shape import WorkspaceShape
from domain.robot import Robot
from domain.command import Command

def run_simulation(workspace: WorkspaceShape, robots_info: list[tuple[Robot, list[Command]]]) -> list[str]:
    results = []
    occupied_positions = set()
    
    for robot, commands in robots_info:
        if robot.position in occupied_positions:
            print(f'Warning: Robot starts at occupied position {robot.position}. Skipping robot')
            continue
        
        for command in commands:
            match command:
                case Command.MOVE:
                    next_position = robot.position.move(robot.orientation)
                    
                    if not workspace.is_valid_position(next_position):
                        print(f'Invalid move: {next_position} is outside the workspace boundaries')
                        continue  # skip invalid move
                    if next_position in occupied_positions:
                        print(f'Blocked: {next_position} is already occupied. Skipping move')
                        continue
                    
                    occupied_positions.discard(robot.position)
                    occupied_positions.add(next_position)
                    robot.position = next_position
                    
                case Command.LEFT:
                    robot.turn_left()
                case Command.RIGHT:
                    robot.turn_right()
        
        occupied_positions.add(robot.position)
        results.append(str(robot))
    
    return results
                    
                