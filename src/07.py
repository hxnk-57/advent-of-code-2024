from itertools import product
from typing import List

file_path = "input/07.txt"

with open(file_path, 'r') as file:    
    lines = [line for line in file]

data = []

for line in lines:
    output, inputs = line.strip().split(":")
    data.append((int(output), list(map(int, inputs.split()))))
    

def create_equations(desired_output: int, inputs: List[int], operators: List[str]) -> int:    
    operator_count = len(inputs)-1
    operator_combinations = product(operators, repeat=operator_count)
    for operator_combo in operator_combinations:
        if valid_equation(desired_output, inputs, operator_combo):
            return desired_output
        else:
            continue
    return 0


def valid_equation(desired_output: int, inputs: List[int], operations: List[str]) -> bool:
    total = inputs[0]
    for index, operator in enumerate(operations):
        if operator == "add":
            total += inputs[index + 1]
        if operator == "multiply":
            total *= inputs[index + 1]
        if operator == "pipe":
            total = int(f"{total}{inputs[index + 1]}")
    return total == desired_output


def part_one() -> int:
    total = 0
    for output, inputs in data:
        total += create_equations(output, inputs, ["add", "multiply"]) 
    return total


def part_two() -> int:
    total = 0
    for output, inputs in data:
        total += create_equations(output, inputs, ["add", "multiply", "pipe"]) 
    return total


if __name__ == "__main__":
    print(f"Part One: {part_one()}") # 1298103531759
    print(f"Part Two: {part_two()}") # 140575048428831