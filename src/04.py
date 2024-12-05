from typing import List

file_path = "input/04.txt"

grid = [List[str]]

with open(file_path, 'r') as file:
    rows = [line.strip() for line in file]
    grid = [[char for char in line] for line in rows]

ROWS, COLUMNS = len(grid), len(grid[0])

def part_one() -> int:
    total = 0
    for row in range(ROWS):
        for column in range(COLUMNS):
            if column + 3 < COLUMNS and grid[row][column:column+4] == ["X", "M", "A", "S"]:   #Horizontal
                total+=1
            if row + 3 < ROWS and grid[row][column]=='X' and grid[row +1][column]=='M' and  grid[row +2][column]=='A' and  grid[row+3][column]=='S':   #Vertical
                total+=1
            if row + 3 < ROWS and column + 3 < COLUMNS and grid[row][column]=='X' and grid[row+1][column+1]=='M' and  grid[row+2][column+2]=='A' and  grid[row+3][column+3]=='S':   #Down-right Diagonal
                total+=1
            if row + 3 < ROWS and column-3>=0 and grid[row][column]=='X' and grid[row+1][column-1]=='M' and  grid[row+2][column-2]=='A' and  grid[row+3][column-3]=='S':   #Down-left Diagonal
                total+=1
            if column - 3>=0 and grid[row][column]=='X' and grid[row][column-1]=='M' and  grid[row][column-2]=='A' and  grid[row][column-3]=='S':   #Horizontal-Reverse
                total+=1
            if row - 3>=0 and grid[row][column]=='X' and grid[row-1][column]=='M' and  grid[row-2][column]=='A' and  grid[row-3][column]=='S':   #Vertical-Reverse
                total+=1
            if row - 3>=0 and column - 3 >= 0 and grid[row][column]=='X' and grid[row-1][column-1]=='M' and  grid[row-2][column-2]=='A' and  grid[row-3][column-3]=='S':   #Up-left Diagonal
                total+=1
            if row - 3 >=0 and column + 3 < COLUMNS and grid[row][column]=='X' and grid[row-1][column+1]=='M' and  grid[row-2][column+2]=='A' and  grid[row-3][column+3]=='S':   #Up-right Diagonal
                total+=1
    return total


def part_two() -> int:
    patterns = [("M", "A", "S"), ("S", "A", "M")]
    total = 0
    for row in range(1, ROWS - 1):
        for column in range(1, COLUMNS - 1):
            if grid[row][column] == "A":
                top_left = grid[row - 1][column - 1]
                bottom_right = grid[row + 1][column + 1]
                top_right = grid[row - 1][column + 1]
                bottom_left = grid[row + 1][column - 1]

                left_diagonal = (top_left, "A", bottom_right)
                right_diagonal = (top_right, "A", bottom_left)

                if left_diagonal in patterns and right_diagonal in patterns:
                    total += 1
    return total


if __name__ == "__main__":
    print(f"Part One: {part_one()}") #2530
    print(f"Part Two: {part_two()}") #1921