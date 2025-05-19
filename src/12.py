file_path = "input/12.txt"

with open(file_path, 'r') as file:
        rows = [line.strip() for line in file]

def display_grid(grid):
    for row in grid:
        print("".join(row))

grid = [[column for column in row] for row in rows]

ROWS, COLUMNS = len(grid), len(grid[0])


def calculate_perimeter(row, column, plant_type):
    perimeter = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_column = row + dr, column + dc
        if new_row < 0 or new_row >= ROWS or new_column < 0 or new_column >= COLUMNS:
            perimeter += 1
        elif grid[new_row][new_column] != plant_type:
            perimeter += 1
    return perimeter


def calculate_sides(row, column, plant_type, grid):
    rows, columns = len(grid), len(grid[0])
    # row and up/down
    # column and left/right
    sides = set()


    return len(sides)

def score(row, column, plant_type, grid, visited):
    plant_locations = set()
    connected = set()
    plant_locations.add((row, column))
    visited[row][column] = True

    while plant_locations:
        r, c = plant_locations.pop()
        connected.add((r, c))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_column = r + dr, c + dc
            if (0 <= new_row < ROWS and 0 <= new_column < COLUMNS and
                grid[new_row][new_column] == plant_type and not visited[new_row][new_column]):
                plant_locations.add((new_row, new_column))
                visited[new_row][new_column] = True

    perimeter = 0
    for r, c in connected:
        perimeter += calculate_perimeter(r, c, plant_type)

    area = len(connected)
    print(f"{plant_type}: Area = {area}, Perimeter = {perimeter}, Score = {area * perimeter}")
    return area * perimeter

def part_one(file_path):
    visited = [[False for _ in range(COLUMNS)] for _ in range(ROWS)]
    total_score = 0

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if not visited[row][column]:
                total_score += score(row, column, grid[row][column], grid, visited)

    print("Total Score:", total_score)
    return total_score


def part_two(file_path):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    total_score = 0

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if not visited[row][column]:
                total_score += score(row, column, grid[row][column], grid, visited)

    print("Total Score:", total_score)
    return total_score


if __name__ == "__main__":
    print(f"Part One: {part_one(file_path)}") # 1449902
   # print(f"Part Two: {part_two(file_path)}") # 