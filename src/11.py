file_path = "input/11.txt"

with open(file_path, 'r') as file:    
    input = file.read().strip()
    rocks = [int(x) for x in input.split()]

encountered = {}

def calculate_result(rock, steps):
    if (rock, steps) in encountered:
        return encountered[(rock, steps)]
    if steps == 0:
        result = 1
    elif rock == 0:
        result = calculate_result(1, steps - 1)
    elif len(str(rock)) % 2 == 0:
        mid_point = len(str(rock)) // 2
        left_rock = str(rock)[:mid_point]
        right_rock = str(rock)[mid_point:]
        result =  calculate_result(int(left_rock), steps-1) + calculate_result(int(right_rock), steps-1)
    else:
        result = calculate_result(rock * 2024, steps-1)
    encountered[(rock, steps)] = result
    return result


def part_one() -> int:
    return sum(calculate_result(rock, 25) for rock in rocks)


def part_two() -> int:
    return sum(calculate_result(rock, 2) for rock in rocks)


if __name__ == "__main__":
    print(f"Part One: {part_one()}") # 233050
    print(f"Part Two: {part_two()}") # 276661131175807
    print(encountered)