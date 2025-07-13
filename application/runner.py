from domain.shape import WorkspaceShape
from domain.robot import Robot
from domain.command import Command
from utils.logging_config import get_logger

logger = get_logger(__name__)

def run_simulation(workspace: WorkspaceShape, robots_info: list[tuple[Robot, list[Command]]]) -> list[str]:
    results = []
    occupied_positions = set()
    
    for i, (robot, commands) in enumerate(robots_info, start=1):
        if robot.position in occupied_positions:
            logger.warning(f'Robot {i} starts at occupied position {robot.position}. Skipping robot')
            continue
        
        for command in commands:
            match command:
                case Command.MOVE:
                    next_position = robot.position.move(robot.orientation)
                    
                    if not workspace.is_valid_position(next_position):
                        logger.warning(f'Robot {i} move invalid: {next_position} is outside the workspace boundaries')
                        continue  # skip invalid move
                    if next_position in occupied_positions:
                        logger.warning(f'Robot {i} blocked: {next_position} is already occupied. Skipping move')
                        continue
                    
                    logger.info(f'Robot {i} moving from {robot.position} to {next_position} facing {robot.orientation}')
                    occupied_positions.discard(robot.position)
                    occupied_positions.add(next_position)
                    robot.position = next_position
                    
                case Command.LEFT:
                    logger.info(f'Robot {i} turning left from {robot.orientation}')
                    robot.turn_left()
                case Command.RIGHT:
                    logger.info(f'Robot {i} turning right from {robot.orientation}')
                    robot.turn_right()
        
        occupied_positions.add(robot.position)
        results.append(str(robot))
    
    return results
                    
                