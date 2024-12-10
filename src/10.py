file_path = "input/10.txt"

grid = [[]]


def find_trail_heads(grid):
    trail_heads = []
    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == 0:
                trail_heads.append((row, column))
    return trail_heads


with open(file_path, 'r') as file:
    rows = [line.strip() for line in file]
    grid = [[int(char) for char in line] for line in rows]

ROWS, COLUMNS = len(grid), len(grid[0])

trail_heads = find_trail_heads(grid)

def calculate_trail_head_score(start, part_2 = False):
    valid_paths = set()

    def explore_path(row, column, path_so_far):
        path_so_far.append((row, column))

        if grid[row][column] == 9:
            if part_2:
                valid_paths.add((row, column))
            else:
                valid_paths.add(tuple(path_so_far))
                
        else:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for row_offset, column_offset in directions:
                new_row = row + row_offset
                new_column = column + column_offset

                if 0 <= new_row < ROWS and 0 <= new_column < COLUMNS:
                    if grid[new_row][new_column] == grid[row][column] + 1 and (new_row, new_column) not in path_so_far:
                        explore_path(new_row, new_column, path_so_far)

        path_so_far.pop()

    explore_path(start[0], start[1], [])

    return len(valid_paths)

def part_one() -> int:
    total = 0
    for head in trail_heads:
        total += calculate_trail_head_score(head)
    return total


def part_two() -> int:
    total = 0
    trail_heads = find_trail_heads(grid)
    for head in trail_heads:
        total += calculate_trail_head_score(head, part_2=True)
    return total


if __name__ == "__main__":
    print(f"Part One: {part_one()}") # 674
    print(f"Part Two: {part_two()}") # 1372