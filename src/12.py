file_path = "input/12.txt"

grid = [[]]

with open(file_path, 'r') as file:    
    rows = [line.strip() for line in file]
    grid = [[pot for pot in line] for line in rows]

ROWS, COLUMNS = len(grid), len(grid[0])

def display_grid(g):
    for r in g:
        print(r)


def deep_copy(g):
    return [row[:] for row in g] 

perimeter_grid = deep_copy(grid)

def calculate_perimiter(row, column, plant_type):
    perimeter = 0
    # Check all four sides for boundaries or different plant types
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, column + dc
        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLUMNS:
            # Out of bounds contributes to the perimeter
            perimeter += 1
        elif perimeter_grid[nr][nc] != plant_type:
            # Neighboring cell is of a different type
            perimeter += 1

    return perimeter


def score(row, column, plant_type) -> int:
    plant_locations = set()
    connected = set()  # To track visited cells

    # Start from the initial cell
    plant_locations.add((row, column))
    grid[row][column] = -1  # Mark as visited

    while plant_locations:
        r, c = plant_locations.pop()
        connected.add((r, c))

        # Check all four neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < ROWS and 0 <= nc < COLUMNS and 
                grid[nr][nc] == plant_type and (nr, nc) not in connected):
                plant_locations.add((nr, nc))
                grid[nr][nc] = -1  # Mark as visited

    perimiter = 0
    for r, c  in connected:
        perimiter += calculate_perimiter(r, c, plant_type)

    area = len(connected)

    print(plant_type, ":", area ,"x", perimiter, "=", area * perimiter)
    return area * perimiter

    
def part_one() -> int:
    total = 0
    current_plant = ""
    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] != current_plant and grid[row][column] != -1:
                current_plant = grid[row][column]
                total += score(row, column, current_plant)
            display_grid(grid)
    return total


def part_two() -> int:
    return 

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")