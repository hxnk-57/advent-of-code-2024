file_path = "input/08.txt"

from collections import defaultdict
import math

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


def colinear(x1, y1, x2, y2, x3, y3):
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area == 0


def valid_distance(d1, d2) -> bool:
    return d1 == 2 * d2 or (d2 == 2 * d1)


def part_one() -> int:
    anti_nodes = set()
    for candidate_row in range(ROWS):
        for candidate_column in range(COLUMNS):
            for _, coordinates in antennas.items():
                for (antenna_1_row, antenna_1_column) in coordinates:
                    for (antenna_2_row, antenna_2_column) in coordinates:
                        if (antenna_1_row, antenna_1_column) == (antenna_2_row, antenna_2_column):
                            continue

                        d1 = math.sqrt((candidate_row - antenna_1_row) ** 2 + (candidate_column - antenna_1_column) ** 2)
                        d2 = math.sqrt((candidate_row - antenna_2_row) ** 2 + (candidate_column - antenna_2_column) ** 2)

                        if colinear(antenna_1_row, antenna_1_column, antenna_2_row, antenna_2_column, candidate_row, candidate_column) and valid_distance(d1, d2):
                            anti_nodes.add((candidate_row, candidate_column))               
    return len(anti_nodes)

def part_two() -> int:
    anti_nodes = set()
    for candidate_row in range(ROWS):
        for candidate_column in range(COLUMNS):
            for _, coordinates in antennas.items():
                for (antenna_1_row, antenna_1_column) in coordinates:
                    for (antenna_2_row, antenna_2_column) in coordinates:
                        if (antenna_1_row, antenna_1_column) == (antenna_2_row, antenna_2_column):
                            continue

                        if colinear(antenna_1_row, antenna_1_column, antenna_2_row, antenna_2_column, candidate_row, candidate_column):
                            anti_nodes.add((candidate_row, candidate_column))

    return len(anti_nodes) 

if __name__ == "__main__":
    print(f"Part One: {part_one()}") # 291
    print(f"Part Two: {part_two()}") # 1015
