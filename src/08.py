file_path = "input/08.txt"

from collections import defaultdict

grid = [[]]

with open(file_path, 'r') as file:    
    rows = [line.strip() for line in file]
    grid = [[char for char in line] for line in rows]

ROWS, COLUMNS = len(grid), len(grid[0])

antennas = defaultdict(list)

for row in range(ROWS):
    for column in range(COLUMNS):
        if grid[row][column] != '.':
            antennas[grid[row][column]].append((row,column))



def valid_distance(dr1, dc1, dr2, dc2) -> bool:
    return dr1 * dc2 == dc1 * dr2


def part_one() -> int:
    anti_nodes = set()
    for row in range(ROWS):
        for column in range(COLUMNS):
            for antenna, coordinates in antennas.items():
                for (antenna_1_row, antenna_1_column) in coordinates:
                    for (antenna_2_row, antenna_2_column) in coordinates:
                        if (antenna_1_row, antenna_1_column) == (antenna_2_row, antenna_2_column):
                            continue

                        d1 = abs(row - antenna_1_row) + abs(column - antenna_1_column)
                        d2 = abs(row - antenna_2_row) + abs(column - antenna_2_column)

                        dr1, dc1 = row - antenna_1_row, column - antenna_1_column
                        dr2, dc2 = row - antenna_2_row, column - antenna_2_column
                        
                        if valid_distance(dr1, dc1, dr2, dc2) and ((d1 == 2 * d2) or (d2 == 2 * d1)):
                            anti_nodes.add((row, column))
                        
    return len(anti_nodes)

def part_two() -> int:
    anti_nodes = set()
    for row in range(ROWS):
        for column in range(COLUMNS):
            for antenna, coordinates in antennas.items():
                for (antenna_1_row, antenna_1_column) in coordinates:
                    for (antenna_2_row, antenna_2_column) in coordinates:
                        if (antenna_1_row, antenna_1_column) == (antenna_2_row, antenna_2_column):
                            continue

                        dr1, dc1 = row - antenna_1_row, column - antenna_1_column
                        dr2, dc2 = row - antenna_2_row, column - antenna_2_column

                        if collinear(dr1, dc1, dr2, dc2):
                            anti_nodes.add((row, column))

    return len(anti_nodes) 

if __name__ == "__main__":
    print(f"Part One: {part_one()}") # 291
    print(f"Part Two: {part_two()}") # 1015
