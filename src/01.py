from typing import Counter

file_path = "input/01.txt"

with open(file_path, 'r') as file:    
    lines = [line.strip() for line in file]

left_list = []
right_list = []

def part_one() -> int:
    for line in lines:
        left_number, right_number = map(int, line.split())
        left_list.append(left_number)
        right_list.append(right_number)

    left_list.sort()
    right_list.sort()

    return sum(abs(left - right) for left, right in zip(left_list, right_list))

def part_two() -> int:
    total = 0
    counter = Counter()
    for r in right_list:
        counter[r] += 1
        
    for l in left_list:
        total += l * counter.get(l, 0)
    return total


print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")