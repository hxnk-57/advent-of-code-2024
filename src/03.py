import re

file_path = "input/03.txt"

with open(file_path, 'r') as file:
    content = file.read().strip()

def calculate_score(text: str) -> int:
    total = 0
    for i in range(len(text)):
        matches = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', text[i:])
        if matches:
            arg_1, arg_2 = int(matches.group(1)), int(matches.group(2))
            total += arg_1 * arg_2
    return total    


def part_one() -> int:
    return calculate_score(content)


def part_two() -> int:
    segments = ("do()" + content).split("don't()")
    clean_text = "".join(segment[segment.find("do()"):] for segment in segments)
    return calculate_score(clean_text)

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")