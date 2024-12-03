import re

file_path = "input/03.txt"

content = open(file_path).read().strip()

def part_one() -> int:
    total = 0
    for i in range(len(content)):
        matches = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', content[i:])
        if matches:
            arg_1 = int(matches.group(1))
            arg_2 = int(matches.group(2))
            total += arg_1 * arg_2
    return total


def part_two() -> int:
    active = True
    total = 0
    for i in range(len(content)):
        if content[i:].startswith("do()"):
            active = True
        if content[i:].startswith("don't()"):
            active = False
        matches = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', content[i:])
        if matches and active:
            arg_1 = int(matches.group(1))
            arg_2 = int(matches.group(2))
            total += arg_1 * arg_2 
    return total

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")