import sys
from application.parser import parse_input
from application.runner import run_simulation

def main():
    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    
    try:
        grid, robots_info = parse_input(input_lines)
        results = run_simulation(grid, robots_info)
        
        for result in results:
            print(result)
    except ValueError as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)
    
if __name__ == '__main__':
    main()