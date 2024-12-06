from itertools import cycle

file_path = "input/06.txt"

with open(file_path, 'r') as file:
    rows = [line.strip() for line in file]
    grid = [[char for char in line] for line in rows]

ROWS = len(grid)
COLUMNS = len(grid[0])

positions_visited = set()

for row in range(ROWS):
    for column in range(COLUMNS):
        if grid[row][column] == "^":
            guard_start = (row, column)
            positions_visited.add(guard_start)


def valid_move(grid, row, column):
    return not grid[row][column] == "#"
        

def guard_escapes(candidate_row, candidate_column) -> bool:
    return (candidate_row < 0) or (candidate_row >= ROWS) or (candidate_column < 0) or (candidate_column >= COLUMNS)


def display_grid(grid):
    for line in grid:
        print(line)


def part_one() -> int:
    direction_cycle = cycle(["right", "down", "left", "up"])
    guard_position = guard_start
    direction = "up"
    while True:
        candidate_row, candidate_column = guard_position
        
        if direction == "up":
            candidate_row -= 1
        if direction == "down":
            candidate_row += 1
        if direction == "left":
            candidate_column -= 1
        if direction == "right":
            candidate_column += 1
        
        if guard_escapes(candidate_row, candidate_column):
            break

        if valid_move(grid, candidate_row, candidate_column):
            positions_visited.add((candidate_row, candidate_column))
            guard_position = candidate_row, candidate_column
        else:
            direction =  next(direction_cycle)
    
    return len(positions_visited)


def part_two():
    total = 0
    # remove the starting position since we can't place an obstacle here
    positions_visited.discard(guard_start)

    for position in positions_visited:
        direction_cycle = cycle(["right", "down", "left", "up"])
        # Create a deep copy of the original grid
        modified_grid = [row[:] for row in grid]
        # Place an obstacle along the existing route:
        modified_grid[position[0]][position[1]] = "#"
        # create a new route
        route = set() 
        # set initial direction
        direction = "up"
        # move the guard back to the start
        guard_position = (guard_start[0], guard_start[1], direction)

        while True:
            candidate_row, candidate_column = guard_position[0], guard_position[1]            
            if direction == "up":
                candidate_row -= 1
            if direction == "down":
                candidate_row += 1
            if direction == "left":
                candidate_column -= 1
            if direction == "right":
                candidate_column += 1
            
            # the current route isn't a cycle, since the gaurd can escape
            if guard_escapes(candidate_row, candidate_column):
                break
            # Check if have made a collision:
            if valid_move(modified_grid, candidate_row, candidate_column):
                # move the guard to the new position
                guard_position = (candidate_row, candidate_column, direction)
                # check if the guard has been in this position to determine if it is a cycle
                if guard_position in route:
                    total += 1
                    break
                route.add(guard_position)
            else:
                direction =  next(direction_cycle)
    return total
    

if __name__ == "__main__":
    print(f"Part One: {part_one()}") # 4967
    print(f"Part Two: {part_two()}") # 1789