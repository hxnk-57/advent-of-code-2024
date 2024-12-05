from typing import List

file_path = "input/05.txt"

rules = []
updates = []
invalid_updates = []

with open(file_path, 'r') as file:    
    lines = [line.strip() for line in file]
    divide = lines.index("")

for line in lines[:divide]:
    rules.append(line.split("|"))

for line in lines[divide + 1:]:
    updates.append(line.strip())


def middle_element_sum(list : List[str]) -> int:
    total = 0
    for element in list:
        middle_element = element[len(element) // 2]
        total += int(middle_element)
    return total


def part_one() -> int:
    filtered_updates = []
    for update in updates:
        valid = True
        for rule in rules:
            first, second = rule
            if first in update and second in update:
                if update.index(first) > update.index(second):
                    valid = False
                    break
        if valid:
            filtered_updates.append(update.split(','))
        else:
            invalid_updates.append(update.split(','))

    return middle_element_sum(filtered_updates)


def fix_updates(invalid_updates):
    for update in invalid_updates:
        for rule in rules:
            first, second = rule
            if first in update and second in update:
                first_index = update.index(first)
                second_index = update.index(second)
                if first_index > second_index:
                    update[first_index], update[second_index] = update[second_index], update[first_index]
    return invalid_updates


def part_two() -> int:
    update = fix_updates(invalid_updates)
    for i in range(5):
        update = fix_updates(update)

    return middle_element_sum(update)


if __name__ == "__main__":
    print(f"Part One: {part_one()}") # 4774 143
    print(f"Part Two: {part_two()}") # 6004 123